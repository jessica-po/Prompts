train_fare, bus_fare = list(map(int, input().split()))
print((train_fare + bus_fare // 2))