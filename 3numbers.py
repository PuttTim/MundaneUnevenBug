number1=int(input("Input first number"))
number2=int(input("Input second number"))
number3=int(input("Input third number"))

if number1>=number2:
  largest=number1
elif number2>=number1:
  largest=number2
elif number3>=largest:
  largest=number3

print("Largest number", largest)