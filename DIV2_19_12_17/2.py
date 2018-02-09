n = input()
l = map(int, raw_input().split())
c = map(int, raw_input().split())
j = 2
r, y = [], []
for i in range (10001) :
	r.append([])

for i in range (0, n+1) :
	y.append(c[0])

for i in l :
	r[i].append(j)
	j += 1

cw = 0
	
	
k = 0
f = 0
for i in range (1,n+1) :
	if y[i] != c[i-1] :
		for j in r[i] :
			y[i] = c[i-1]
			y[j] = c[i-1]
			f = 1

	if y == c :
		break
	if f == 1 :
		cw += 1
	f = 0
for i in range(0,n) :
	if c[i] != y[i+1] :
		k += 1
print cw+k+1





