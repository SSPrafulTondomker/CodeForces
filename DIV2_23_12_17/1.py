v1, v2, v3, v4 = map(int, raw_input().split())
if v4 <= v1 and v4 <= v2 and v4 <= v3 and 2*v4 >= v3:
	print v1
	print v2
	print v3
elif v4 <= v1 and v4 <= v2 and v4 > v3 :
	if 2*v3 >= v4 and 2*v4 >= 2*v3 :
		print v1*2
		print v2*2
		print v3*2
	else :
		print "-1"
elif v4 <= v1 and v4 > v2 :
	if 2*v2 >= v4 and 2*v3 >= v4 and 2*v4 >= 2*v3 :
		print v1*2
		print v2*2
		print v3*2
	else :
		print "-1"
elif v4 > v1 :
	if 2*v1 >= v4 and 2*v2 >= v4 and 2*v3 >= v4 and 2*v4 >= 2*v3 :
		print v1*2
		print v2*2
		print v3*2
	else :
		print "-1"
else :
	print "-1"
