n=int(input("enter the limit:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		j=j*i
		print(j,end=" ")
	print("\n")
