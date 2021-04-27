hexa=str(input("Hexa: "))
total=0

i=0

bin3=hexa
lenhexa=len(hexa)

for e in range (lenhexa-1,-1,-1):
  
  print("e:", e)
  print("bin3[i]:", bin3[i])
  if bin3[i] == "0":
    total=total+0*16**e
  elif bin3[i] == "1":
    total=total+1*16**e
  elif bin3[i] == "2":
    total=total+2*16**e
  elif bin3[i] == "3":
    total=total+3*16**e
  elif bin3[i] == "4":
    total=total+4*16**e
  elif bin3[i] == "5":
    total=total+5*16**e
  elif bin3[i] == "6":
    total=total+6*16**e
  elif bin3[i] == "7":
    total=total+7*16**e
  elif bin3[i] == "8":
    total=total+8*16**e
  elif bin3[i] == "9":
    total=total+9*16**e
  elif bin3[i] == "A":
    total=total+10*16**e
  elif bin3[i] == "B":
    total=total+11*16**e
  elif bin3[i] == "C":
    total=total+12*16**e
  elif bin3[i] == "D":
    total=total+13*16**e 
  elif bin3[i] == "E":
    total=total+14*16**e
  elif bin3[i] == "F":
    total=total+15*16**e
  
  i=i+1

print(total)