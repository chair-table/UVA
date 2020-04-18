c = 0
while(1):
	treated = 0
	treat_num = 0
	balance = 0
	p = int(input())
	if (p == 0):
		break

	a = list(map(int,input().split()))
	# n,m=map(int,input().split())
	for i in range(p):
		# a = int(input())
		# a = list(map(int,input().split()))
		if a[i] == 0:
			treated = treated + 1;
		else:
			treat_num = treat_num + 1;

		balance = treat_num - treated

	c = c+1

	# print("Case",c,end = '')
	# print(':', balance)
	print("Case {}: {}".format(c, balance))