l=[]
n=int(input("Enter The Limit : "))
print("Enter ",n," Numbers")
for i in range(0,n):
   no=int(input())
   if no>100:
     l.append("over")
   else:
     l.append(no)

print(l)

