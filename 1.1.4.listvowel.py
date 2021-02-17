l=[]
vowel=['a','e','i','o','u']
str=input("Enter the String : ")
for i in str:
  if  i in vowel and i not in l :
      l.append(i)
print("the vowel Present in the string is  ",l)

