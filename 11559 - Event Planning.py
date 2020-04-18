while(1):
	n, b, h, w =  map(int, input().split())
	# print(n, b, h, w)
	budget = b + 5
	p = []
	for i in range(h):
		p.append(int(input()))
		# for j in range(w):
		# 	room = []
		a = list(map(int, input().split()))
		for j in a:
			if j >= n and p[i]*n <= (budget-5):
				budget = p[i]*n

	if(budget <= b):
		print(str(budget)+"\n")
	else:
		print("stay home\n")

		# print(p, a)
