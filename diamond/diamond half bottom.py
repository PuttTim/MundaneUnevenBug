row=int(input("Enter row number here: "))
column=0
col2=row-1
column3=row
col4=1

for i in range (row):
  column=int(column+1)
  
# for blanks
  for i in range (column):
   print(" ", end='')
  

# for stars
  for i in range (col2+1):
   print("*", end="")
  col2=col2-1

#bottom half




#for stars
  column3=int(column3-1)
  for i in range (column3):
   print("*", end='')
  
#for blanks
  for i in range (col4):
   print(" ", end="")
  col4=col4+1
  print("")
