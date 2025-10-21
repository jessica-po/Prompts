import sys;

nbDancers, nbDances = list(map(int, sys.stdin.readline().split(' ')));
dancers = [0]*(nbDancers+1);

for line in sys.stdin:
	taken = [False, False, False, False];

	ds = list(map(int, line.split(' ')));

	for d in ds:
		taken[dancers[d]] = True;

	for d in ds:
		if dancers[d] == 0:
			if not taken[1]:
				dancers[d] = 1;
				taken[1] = True;
			elif not taken[2]:
				dancers[d] = 2;
				taken[2] = True;
			elif not taken[3]:
				dancers[d] = 3;
				taken[3] = True;

print((' '.join(map(str, dancers[1:]))));