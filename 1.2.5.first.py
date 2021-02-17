def changechar(str):
	char=str[0]
	str= str.replace(char,'$')
	str=char+str[1:]
	return str

str1=input("Enter A String : ")
print(changechar(str1))
