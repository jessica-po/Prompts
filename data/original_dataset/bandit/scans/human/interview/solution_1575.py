import math
import sys

arrival, departure, time_per_client = [int(x) for x in input().split()]
num_clients = int(input())
if num_clients > 0:
	clients_arrival = [int(x) for x in input().split()]
else:
	print(arrival)
	return

best_time = None

current_time = arrival
clients_at_queue = 0

client_to_arrive = 0
client_wait_time = [math.inf for client in clients_arrival]
client_to_leave = 0

while current_time <= departure - time_per_client:
	while client_to_arrive < num_clients and clients_arrival[client_to_arrive] <= current_time:
		clients_at_queue += 1
		client_to_arrive += 1

	if clients_at_queue == 0:
		best_time = current_time
		break
	else:
		clients_at_queue -= 1
		client_wait_time[client_to_leave] = current_time - clients_arrival[client_to_leave]
		client_to_leave += 1

		current_time += time_per_client



while (best_time is None or best_time < 0) and len(client_wait_time) > 0:
	happiest_client = client_wait_time.index(min(client_wait_time))
	best_time = clients_arrival[happiest_client] - 1

	if best_time < 0:
		client_wait_time = client_wait_time[happiest_client+1:]
		clients_arrival = clients_arrival[happiest_client+1:]


print(best_time)