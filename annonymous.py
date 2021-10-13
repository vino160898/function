#annonymous (or) lambda function
#1 normal function:
def disply(no):
	return no*2
result=display(2)
print(result)
#1 annonymous function
result=lambda no:no*2
print(result(5))
#2 normal function
def gratest(no1,no2):
	if no1>no2
		return no1
	else:
		return no2
print(gratest(20,30))
#2 annonymous function
result=lambda no1,no2:no1 if no1>no2 else no2
print(result(100,200))
