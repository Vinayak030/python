n=int(input("EnteR ThE LimiT: "))
a=[]
print("Enter the Words: ")
for i in range(1,n+1):
	str=input()
	a.append(str)
print(a)
max=0
temp=a[0]
for i in a:
    if(len(i)>max):
       max=len(i)
       temp=i
print("The with the longest word is ",temp," and length is:",max)
                                   
