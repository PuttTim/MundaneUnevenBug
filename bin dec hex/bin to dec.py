binary=str(input("Binary: "))
total=0
d=2
for i in range(len(binary)):
  
  if binary[i] > "1":
    print("Error: only 1's and 0's are allowed")
    exit()

r=0
w=len(binary)-1

for e in range(w,-1,-1):
  
  if binary[r] == "1":
    total=total+2**e
  else:total=total+0
  
  

  #print("Binary[r] is:", binary[r])
  r=r+1
  #print("e:",e)
  
  #print("total in loop:",total)
  
print("total final:", total)