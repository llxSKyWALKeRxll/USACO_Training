"""
ID: detrime1
LANG: PYTHON3
TASK: ride
"""

import sys
sys.stdin = open("ride.in","r")
sys.stdout = open("ride.out","w")
ascii1 = [(ord(i)%ord("A")+1) for i in input()]
ascii2 = [(ord(i)%ord("A")+1) for i in input()]
chk1, chk2 = 1, 1
for asc in ascii1:
	chk1 = (chk1*asc)%47
for asc in ascii2:
	chk2 = (chk2*asc)%47
print("GO" if chk1==chk2 else "STAY")