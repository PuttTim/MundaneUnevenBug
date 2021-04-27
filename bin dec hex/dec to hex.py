binary=int(input("Decimal: "))
i=0
full=["x" for i in range (binary)]
remainder=["x" for i in range (binary)]
out="0"

asd="0"
bin2=binary
count=0

strbin=str(binary)


for i in range (binary-1,-1,-1):
  
  bin3=bin2%16
  if bin3 < 10:
    bin3=bin3
  elif bin3 == 10:
    bin3="A"
  elif bin3 == 11:
    bin3="B"
  elif bin3 == 12:
    bin3="C"
  elif bin3 == 13:
    bin3="D" 
  elif bin3 == 14:
    bin3="E"
  elif bin3 == 15:
    bin3="F"
   
  
  bin2=int(bin2/16)

  full[i]=str(bin3)

  
for a in range(binary):
 
  d=str(full[a])
  asd=asd+d

f=asd.lstrip("0")

out=f
print(out)

