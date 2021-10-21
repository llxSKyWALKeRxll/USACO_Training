"""
ID: detrime1
LANG: PYTHON3
TASK: friday
"""

import sys,os.path
from collections import *
if os.path.exists('friday.in'):
    sys.stdin = open('friday.in', 'r')
    sys.stdout = open('friday.out', 'w')

def detri():
	n = int(input())
	weekDays = [0]*7
	monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
	day = 2
	for year in range(1900, 1900+n):
		if str(year)[2:]=="00": 
			if not year%400: monthDays[1] = 29
		elif not year%4: monthDays[1] = 29
		else: monthDays[1] = 28
		for monthDay in monthDays:
			day += 12
			day %= 7
			weekDays[day] += 1
			day += monthDay-12
	print(*weekDays)

	# WORKING GARBAGE WACK BRUTE FORCE
	"""days = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
				months = {
				"JAN":31,
				"FEB":(28,29),
				"MAR":31,
				"APR":30,
				"MAY":31,
				"JUN":30,
				"JUL":31,
				"AUG":31,
				"SEP":30,
				"OCT":31,
				"NOV":30,
				"DEC":31,
				}
				ans = {day:0 for day in days}
				n = int(input())
				day = 0
				for year in range(1900, 1900+n):
					leap = False
					if str(year)[2:]=="00":
						if not year%400:
							leap = True
					else:
						if not year%4:
							leap = True
					months["FEB"] = 29 if leap else 28
					for month in months:
						for i in range(1,months[month]+1):
							day = (day+1)%7
							if i==13:
								ans[days[day]] += 1
				check = []
				for val in ans.values():
					check.append(val)
				check[:] = check[6:]+check[:6]
				print(*check)"""

if __name__ == "__main__":
	detri()