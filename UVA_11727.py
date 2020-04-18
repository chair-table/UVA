p = int(input())
for i in range(p):
	a,b,c=map(int,input().split())	
	if (a>b and b>c) or (c>b and b>a) :
		mid = b;
	elif (b>a and a>c) or (c>a and a>b) :
		mid = a;
	elif (a>c and c>b) or (b>c and c>a) :
		mid = c;
	# print('Case',i+1,':',mid)
	print('Case',i+1, end = '')
	print(':',mid)
	# print('Case ',i+1,': ',mid, end = '')
# 	# print(mid)



# n = int(input())
# for i in range(1,n+1):
#     L = list(map(int,input().split()))
#     L.sort()
#     print("Case "+int(i)+":"+L[1])
#     print("Case {:,}:".format(i),L[1])