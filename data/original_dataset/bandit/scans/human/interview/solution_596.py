import datetime
from pprint import pprint
year, month, day = (int(i) for i in input().split(':'))
x = datetime.date(year, month, day)
year, month, day = (int(i) for i in input().split(':'))
y = datetime.date(year, month, day)
pprint(abs(int((x - y).days)))