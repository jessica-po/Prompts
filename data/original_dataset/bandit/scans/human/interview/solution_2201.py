destination, max_gas_tank_volume, gas_prices_number = list(map(int, input().split()))
start_point = 0
gas_prices = {start_point:0}
for i in range(gas_prices_number):
    coordinate, price = list(map(int, input().split()))
    gas_prices[coordinate] = price
points = sorted(list(gas_prices.keys()), reverse = True)
current_point = start_point
count = 0
gas_tank_volume = max_gas_tank_volume
reachable_points = []
while current_point != destination:
    farthest_reachable_point = current_point + max_gas_tank_volume
    while points and points[-1] <= farthest_reachable_point:
        reachable_points.append(points.pop())
    if reachable_points:
        cheaper_reachable_points = sorted([point for point in reachable_points if gas_prices[point] < gas_prices[current_point]])
        next_point = cheaper_reachable_points[0] if cheaper_reachable_points else min(reachable_points, key = lambda point: gas_prices[point])
        if farthest_reachable_point >= destination and (current_point == start_point or gas_prices[next_point] >= gas_prices[current_point]):
            next_point = destination
        else:
            reachable_points = [point for point in reachable_points if point > next_point]
    else:
        if farthest_reachable_point >= destination:
            next_point = destination
        else:
            count = -1
            break
    distantion = next_point - current_point
    if next_point != destination and gas_prices[current_point] <= gas_prices[next_point]:
        required_gas_volume = max_gas_tank_volume
    else:
        required_gas_volume = distantion
    if required_gas_volume > gas_tank_volume:
        count += (required_gas_volume - gas_tank_volume)*gas_prices[current_point]
        gas_tank_volume = required_gas_volume
    current_point = next_point
    gas_tank_volume -= distantion
print(count)