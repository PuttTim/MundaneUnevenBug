row=int(input("Enter row number here: "))
column=0
col2=row
column3=row
col4=1

for i in range (row):
  column=int(column+1)
  
# for stars
  for i in range (column):
   print("*", end='')
  

# for blanks
  for i in range (col2):
   print("x", end="")
  col2=col2-1

#bottom half




#for blank
  column3=int(column3-1)
  for i in range (column3):
   print("v", end='')
  
#for star
  for i in range (col4):
   print("*", end="")
  col4=col4+1
  print("")

#do bottom half of this (and combine the two)