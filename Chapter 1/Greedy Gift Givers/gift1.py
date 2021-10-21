"""
ID: detrime1
LANG: PYTHON3
TASK: gift1
"""

import sys
from collections import *
sys.stdin = open("gift1.in","r")
sys.stdout = open("gift1.out","w")

def insertName(name, dictMap):
	dictMap[name] = None

def insertData(name,dictMap1, dictMap2):
	a,b = map(int, input().split())
	dictMap1[name] = ((a,b,a)) if not b else ((a//b,a%b,a))
	for i in range(b):
		dictMap2[name].add(input())

def paisaMila(name, dictMap):
	ans[name] += names[name][1]
	ans[name] -= names[name][2]
	for n in receiversEnd[name]:
		ans[n] += names[name][0]

n = int(input())
names = defaultdict()
receiversEnd = defaultdict(set)
for _ in range(n):
	insertName(input(), names)
for i in range(n):
	insertData(input(),names,receiversEnd)
ans = {name: 0 for name in names}
for name in receiversEnd:
	paisaMila(name, ans)
for name in ans:
	print(name, ans[name])