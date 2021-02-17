l=[]
s=0
n=int(input("Enter the Limit:\t"))
print("Enter the ",n," Elements:")
for i in range(0,n):
	no=int(input())
	l.append(no)
print("The List is ",l)
      
for i in range(0,len(l)):
		s=s+l[i]
print("The sum is ",s)      
      
