string =input("Enter The String:\t")
dict={}
for i in string:
    	 if i in dict:
    	 	dict[i] += 1
    	 else:
    	 	dict[i] = 1
print ("The Each Character Count is :\n ",dict)
           
