def fibinocci(n):
	f1=0
	f2=1
	f3=1
	for i in range(0,n):
	    print(f1,end=" ")
	    f1=f2
	    f2=f3
	    f3=f1+f2
                            	    
n=int(input("enter the limit:\t"))
print("the fibinocci series is")
print(fibinocci(n),"\n")

                  
