startYear = int(input("Enter the Current Year: "))

endYear = int(input("Enter the Year u Want to Stop : "))
 
print ("The  leap years are :\n")

for year in range(startYear, endYear+1):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)
