n, m = map(int, raw_input().split())
l = []
l.append(1)
for i in range (1,101) :
	l.append(0)

f = 0
for i in range (n) :
	a, b = map(int, raw_input().split())
	if a == 0 :
		f = 1
	for j in range (a+1,b+1) :
		l[j] = 1
flag = 0

for i in range (m+1) :
	if l[i] == 0 :
		flag = 1

if flag == 1 or f == 0:
	print "NO"

elif f == 1 and flag == 0:
	print "YES"




