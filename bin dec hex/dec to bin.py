binary=int(input("Decimal: "))
i=0
deci=[" " for i in range (binary)]

asd="0"
bin2=binary
count=0

strbin=str(binary)


for i in range (binary-1,-1,-1):
  
  bin3=bin2%2
  bin2=int(bin2/2)

  deci[i]=bin3
  
  #i=i+1
for a in range(binary):
  d=str(deci[a])
  asd=asd+d

out=int(asd)
print(out)