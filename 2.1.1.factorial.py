def factorial(num):
		f=1
		for i in range(1,num+1):
			f=f*i
		return f
		
no=int(input("enter the number:\t"))
print("The factorial of ",no," is",factorial(no))

		
