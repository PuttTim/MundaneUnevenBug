row=int(input("Enter row number here: "))
column=row
col2=1
for i in range (row):

#for blank
  column=int(column-1)
  for i in range (column):
   print("z", end='')
  
#for star
  for i in range (col2):
   print("*", end="")
  col2=col2+1
  print("")


column=row
col2=0
for i in range (row):

# for blanks
  for i in range (col2):
   print("z", end="")
  col2=col2+1

# for stars  
  for i in range (column):
   print("*", end="")
  column=int(column-1)
  print("")
