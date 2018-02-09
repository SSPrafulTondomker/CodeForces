def bfs(s, v, l, r) :
	q = []
	q.append(s)
	while q :
		p = q.pop()
		c = 0
		for i in l[p] :
			if v[i] == 0 :
				if len(l[i]) == 0 :
					c += 1
				else :
					q.append(i)
				v[i] = 1
		#print c
		if c < 3 :
			return 0
	return 1


	
n = input()
l, v = [], []
l.append([])
v.append(0)
for i in range (1, n+1) :
	l.append([])
	v.append(0)
for i in range (1,n) :
	k = input()
	l[k].append(i+1)
p = 0
r = 0

if bfs(1, v, l, r) == 1 :
	print "Yes"
else :
	print "No"



