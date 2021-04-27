num=int(input("Enter amount of numbers here: "))
num2=[0 for i in range(num)]
for i in range (num):
  num2[i]=int(input("Enter number here:"))
  print(num2)
loop=0
loop2=0

for i in range (num-1):

  for j in range (num-1):
    if num2[j] > num2[j+1]:
      temp3=num2[j+1]
      temp4=num2[j]
      num2[j]=temp3
      num2[j+1]=temp4
      loop2=loop2+1
      print(num2, loop2)

print(num2,"=final loop")
