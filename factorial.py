def fact(n):
	f = 1
	for i in range (1, n+1):
		f=f*i
		print("the factorial is % d" %(f))
		n=ent(input("enter a number"))
		fact(n)