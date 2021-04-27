max=0
min=999999999999999999
total=0
count=0
for a in range(2):
  num=int(input("Enter number here:"))
  if num > max:
    max=num
  if num < min:
    min=num
  total=num+total
  count=count+1
  

avg=total/count
print("max:", max)
print("min:", min)
print("total:", total)
print("avg: ", avg)