from sys import stdin,stdout
# stdout = open('output.txt', 'w+')
# stdin = open('input.txt','r+')


from collections import Counter
def prefixsuffixmatch(s):
	pi_table=[0 for i in range(len(s))]
	for i in range(1,len(s)):
		y=pi_table[i-1]
		while s[i]!=s[y] and y!=0:
			y=pi_table[y-1]
		if s[i]==s[y]:
			y+=1
		pi_table[i]=y
	return pi_table
def canprint(a,b):
	if a['0']>=b['0'] and a['1']>=b['1']:
		return True
	return False

def flushit(s):
	if '0' in s:
		stdout.write('0'* s['0'])
	if '1' in s:
		stdout.write('1'* s['1'])
def fillit(x):
	if '0' not in x:
		x['0']=0
	if '1' not in x:
		x['1']=0
	return x
	
s=stdin.readline().strip();counter_s=fillit(Counter(s))
t=stdin.readline().strip();counter_t=fillit(Counter(t))
t_pi_table=prefixsuffixmatch(t)
longest_match=t_pi_table[-1]

repeating_part=t[longest_match:]

counter_repeating_part=fillit(Counter(repeating_part))




if len(counter_s)==2 and len(counter_t)==2:
	if counter_s['0']>=counter_t['0'] and counter_s['1']>=counter_t['1']:
		stdout.write(t);counter_s['0']-=counter_t['0'];counter_s['1']-=counter_t['1'];


	# while canprint(counter_s,counter_repeating_part)==True:
	# 	stdout.write(repeating_part);
	# 	counter_s['0']-=counter_repeating_part['0'];
	# 	counter_s['1']-=counter_repeating_part['1'];

	if '0' in counter_repeating_part and '1' in counter_repeating_part:
		if counter_repeating_part['0']>0 and counter_repeating_part['1']>0:
			r=min(counter_s['0']//counter_repeating_part['0'],counter_s['1']//counter_repeating_part['1'])
			stdout.write(repeating_part*r);
			counter_s['0']-=(r*counter_repeating_part['0']);
			counter_s['1']-=(r*counter_repeating_part['1']);
	flushit(counter_s);