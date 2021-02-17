l1=[]
l2=[]

m=int(input("Enter the First Limit : "))
print("Enter ",m," Elements")
for i in range(0,m):
	no=int(input())
	l1.append(no)
	
n=int(input("Enter Second limit : "))
print("Enter ",n," Elements")
for i in range(0,n):
	no=int(input())
	l2.append(no)
	
if len(l1)==len(l2):
	print("The Lists are of Equal Length")
else:
	print("The Lists are of Different Length")
	
	
if sum(l1)==sum(l2):
	print("The Lists are of  Equal sum ",sum(l1))
else:
	print("The Lists are of Different sum ",sum(l1),sum(l2))
	

c=set(l1).intersection(set(l2))
if c!=0:
	print("The Common Values : ",c)
else:
	print("No common Values")
                                           
