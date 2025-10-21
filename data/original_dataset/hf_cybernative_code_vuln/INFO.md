This dataset is available on [huggingface](https://huggingface.co/datasets/CyberNative/Code_Vulnerability_Security_DPO) and is a dataset of synthetic Data programming by Demonstration (DPO) pairs, focusing on the relationships between secure and insecure code across many programming languages.

It is generated using this deepseek model: [LoneStriker/deepseek-coder-33b-instruct-4.0bpw-h6-exl2](https://huggingface.co/LoneStriker/deepseek-coder-33b-instruct-4.0bpw-h6-exl2)

Languages Used:
* C++
* Python
* Java
* JavaScript
* C#
* PHP
* Ruby
* Swift
* Go
* Kotlin
* Fortran

Schema:
* Vulnerable Code: A code snippet that contains a specific vulnerability, written in a professional, realistic manner but intentionally insecure and inefficient.
* Fixed Code: A secure and optimized version of the vulnerable code, adhering to best practices and efficient methods.
* Task Description: A high-level instruction that applies to both the vulnerable and fixed code, providing context and serving as a question for model evaluation.