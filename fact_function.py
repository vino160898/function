def factorial(no):
	fact=1
	while no>=1:
		fact=fact*no
		no-=1
	else:
		print(fact)
for no in range(5,0,-1):
	factorial(no)
