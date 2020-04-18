TC = int(input())
for x in range(TC):
	a,b=map(int,input().split())
	# x, y, z = [int(x) for x in input().split()]  
	# print(x, y, z)

	if(a>b):
		print(">")
	elif(a<b):
		print("<")
	else:
		print("=")
