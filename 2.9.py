total=0
count=int(input("Enter the number of numbers to follow: "))
for counter in range (count):
 number=int(input("Enter number here: "))
 if number>=0:
   total=total+number
   
print(total)
