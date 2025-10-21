speeds = [1000000]
overtakes = [True]
count = 0
speed = 0
n = int(input())
for e in range(n):
  inp = list(map(int, input().split()))
  # print(inp)
  if inp[0] == 4:
    overtakes.append(True)
  elif inp[0] == 6:
    overtakes.append(False)
  elif inp[0] == 5:
    speeds.append(1000000)
  elif inp[0] == 3:
    speeds.append(inp[1])
    while speed > speeds[-1]:
      count += 1
      speeds.pop()
      
  elif inp[0] == 2:
    while not overtakes[-1]:
      count += 1
      overtakes.pop()
  else:
    while inp[1] > speeds[-1]:
      count += 1
      speeds.pop()
    speed = inp[1]
  
print(count)
"""
Polycarp changes the speed of his car to specified (this event comes with a positive integer number);
Polycarp's car overtakes the other car;
Polycarp's car goes past the "speed limit" sign (this sign comes with a positive integer);
Polycarp's car goes past the "overtake is allowed" sign;
Polycarp's car goes past the "no speed limit";
Polycarp's car goes past the "no overtake allowed";
"""