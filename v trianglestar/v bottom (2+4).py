row=int(input("Enter row number here: "))
column=row
col2=0
column3=row
col4=0


for i in range (row):


# for stars
  for i in range (column):
    print("*", end='')
  column=int(column-1)
  

# for blanks
  for i in range (col2):
    print("x", end='')
  col2=col2+1  
  

#bottom half

# for blanks
  for i in range (col4):
   print("z", end="")
  col4=col4+1

# for stars  
  for i in range (column3):
   print("*", end="")
  column3=int(column3-1)
  print("")
