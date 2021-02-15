l=[]
n=int(input("Enter The Limit: "))
print("Enter the Elements:\n")
for i in range(0,n):
	no=int(input())
	l.append(no)
print("The Elements are \n",l)
print("The positive nos are \n")
for i in l:
	if(0<i):
		print(i)
