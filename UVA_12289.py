p = int(input())
for i in range(p):
	on = 0
	tw = 0
	one = 'one'
	two = 'two'
	three = 'three'
	a = input()
	length = len(a);
	if length == 3:
		for i in range(length):
			if a[i] == one[i]:
				on += 1
			if a[i] == two[i]:
				tw += 1
		if on == 3 or on == 2:
			print("1")
		else:
			print("2")
	else:
		print("3")