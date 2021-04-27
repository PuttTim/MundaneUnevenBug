num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

import random



if num1>num2:
  large=num1
else:large=num2
print("large:", large)
for i in range(large):
  final=random.randint(num1,num2)
  num1=int(input("Enter number here"))
  print(final)
  

