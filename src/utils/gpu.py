from __future__ import annotations

import os
import shutil
import subprocess
import threading
import time
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

try:
    import torch
except Exception:  # pragma: no cover - torch may not be installed in all contexts
    torch = None  # type: ignore


def _which(cmd: str) -> Optional[str]:
    path = shutil.which(cmd)
    return path


def _run(cmd: List[str], timeout: float = 5.0) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            encoding="utf-8",
            timeout=timeout,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except Exception as e:  # pragma: no cover
        return 1, "", str(e)


def nvidia_smi_available() -> bool:
    return _which("nvidia-smi") is not None


def query_gpu_snapshot() -> List[Dict[str, Any]]:
    """Return a list of GPU metrics using nvidia-smi if available, else torch.

    Fields: index, name, memory_used_mb, memory_total_mb, utilization_pct, power_w, temp_c
    """
    if nvidia_smi_available():
        rc, out, _ = _run(
            [
                "nvidia-smi",
                "--query-gpu=index,name,memory.total,memory.used,utilization.gpu,power.draw,temperature.gpu",
                "--format=csv,noheader,nounits",
            ]
        )
        if rc == 0 and out:
            rows = []
            for line in out.splitlines():
                # Expect: idx, name, mem.total (MB), mem.used (MB), util (%), power (W), temp (C)
                parts = [p.strip() for p in line.split(",")]
                if len(parts) >= 7:
                    try:
                        rows.append(
                            {
                                "index": int(parts[0]),
                                "name": parts[1],
                                "memory_total_mb": float(parts[2]),
                                "memory_used_mb": float(parts[3]),
                                "utilization_pct": float(parts[4]),
                                "power_w": float(parts[5]),
                                "temp_c": float(parts[6]),
                            }
                        )
                    except Exception:
                        # Skip malformed rows
                        continue
            return rows

    # Fallback: torch-only approximate metrics
    results: List[Dict[str, Any]] = []
    if torch is not None and hasattr(torch, "cuda") and torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        for idx in range(device_count):
            name = torch.cuda.get_device_name(idx)
            torch.cuda.synchronize(device=idx)
            # memory stats in bytes
            try:
                mem_alloc = torch.cuda.memory_allocated(idx) / (1024 * 1024)
                mem_reserved = torch.cuda.memory_reserved(idx) / (1024 * 1024)
            except Exception:
                mem_alloc, mem_reserved = 0.0, 0.0
            results.append(
                {
                    "index": idx,
                    "name": name,
                    "memory_total_mb": None,
                    "memory_used_mb": float(mem_reserved or mem_alloc),
                    "utilization_pct": None,
                    "power_w": None,
                    "temp_c": None,
                }
            )
    return results


def log_gpu_overview(logger) -> None:
    """Log a one-time overview of GPU environment."""
    if torch is not None:
        try:
            logger.info(f"torch: {torch.__version__} cuda_available: {torch.cuda.is_available()}")
            if torch.cuda.is_available():
                count = torch.cuda.device_count()
                names = [torch.cuda.get_device_name(i) for i in range(count)]
                logger.info(f"CUDA device count: {count} | devices: {names}")
        except Exception as e:
            logger.info(f"torch cuda probe failed: {e}")

    if nvidia_smi_available():
        rc, driver_out, _ = _run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"], timeout=5)
        driver = driver_out.splitlines()[0] if rc == 0 and driver_out else "?"
        rc2, cuda_out, _ = _run(["nvidia-smi"], timeout=5)
        cuda_ver = None
        if rc2 == 0 and cuda_out:
            for line in cuda_out.splitlines():
                if "CUDA Version" in line:
                    try:
                        cuda_ver = line.split("CUDA Version:")[-1].strip().split(" ")[0]
                    except Exception:
                        pass
                    break
        logger.info(f"nvidia-smi available | driver: {driver} | cuda: {cuda_ver or '?'}")
        snapshot = query_gpu_snapshot()
        if snapshot:
            for entry in snapshot:
                logger.info(
                    "GPU %s | %s | mem %s/%s MB | util %s%% | power %s W | temp %s C"
                    % (
                        entry.get("index"),
                        entry.get("name"),
                        _fmt(entry.get("memory_used_mb")),
                        _fmt(entry.get("memory_total_mb")),
                        _fmt(entry.get("utilization_pct")),
                        _fmt(entry.get("power_w")),
                        _fmt(entry.get("temp_c")),
                    )
                )


def _fmt(val: Any) -> str:
    if val is None:
        return "?"
    try:
        if isinstance(val, float):
            return f"{val:.1f}"
        return str(val)
    except Exception:
        return "?"


@dataclass
class PeriodicGpuMonitor:
    """Background GPU monitor that logs metrics at a fixed interval."""

    interval_sec: float = 30.0
    logger: Any = None
    enabled: bool = True

    def __post_init__(self) -> None:
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        if self.logger is None:
            import logging

            self.logger = logging.getLogger(__name__)

    def start(self) -> None:
        if not self.enabled:
            return
        if self._thread is not None:
            return

        def _loop() -> None:
            while not self._stop.is_set():
                try:
                    snap = query_gpu_snapshot()
                    if snap:
                        lines = []
                        for e in snap:
                            lines.append(
                                "GPU %s | %s | mem %s/%s MB | util %s%% | power %s W | temp %s C"
                                % (
                                    e.get("index"),
                                    e.get("name"),
                                    _fmt(e.get("memory_used_mb")),
                                    _fmt(e.get("memory_total_mb")),
                                    _fmt(e.get("utilization_pct")),
                                    _fmt(e.get("power_w")),
                                    _fmt(e.get("temp_c")),
                                )
                            )
                        self.logger.info(" | ".join(lines))
                except Exception:
                    # Never crash the app due to monitor issues
                    pass
                finally:
                    self._stop.wait(self.interval_sec)

        self._thread = threading.Thread(target=_loop, name="gpu-monitor", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._thread is None:
            return
        self._stop.set()
        self._thread.join(timeout=max(1.0, self.interval_sec))
        self._thread = None


