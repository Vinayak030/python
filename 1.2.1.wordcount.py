def wordcount(str): 
   text=str.split()
   count=dict()
   for i in text:
      if i in count:
         count[i]=count[i]+1
      else :
         count[i]=1
   return count
 
str1=input("Enter The  String: ")
print(wordcount(str1))
