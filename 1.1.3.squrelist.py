l=[]
n=int(input("Enter the limit: "))
print("Enter the Numbers : \n")
for i in range(0,n):
	no=int(input())
	l.append(no)
for i in l:
	print("The squre of ",i,"=",i*i)
