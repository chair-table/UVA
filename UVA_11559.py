def main():
	try:
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

				# if 

			if(budget <= b):
				print(budget)
			else:
				print("stay home")
	except EOFError:
        pass

if __name__=="__main__":
    main()

		# print(p, a)












# while(1):
# 	p = int(input())
# 	if (p == 0):
# 		break

# 	n,m=map(int,input().split())
# 	for i in range(p):
# 		x,y=map(int,input().split())	
# 		if (n==x or m==y) :
# 			print('divisa')
# 		elif (x>n and y>m):
# 			print('NE') 
# 		elif (x>n and y<m):
# 			print('SE')
# 		elif (x<n and y>m):
# 			print('NO')
# 		else:
# 			print('SO')