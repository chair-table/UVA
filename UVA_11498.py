while(1):
	p = int(input())
	if (p == 0):
		break

	n,m=map(int,input().split())
	for i in range(p):
		x,y=map(int,input().split())	
		if (n==x or m==y) :
			print('divisa')
		elif (x>n and y>m):
			print('NE') 
		elif (x>n and y<m):
			print('SE')
		elif (x<n and y>m):
			print('NO')
		else:
			print('SO')