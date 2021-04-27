row=int(input("Enter row number here: "))
column=row
col2=1
for i in range (row):

#for blank
  column=int(column-1)
  for i in range (column):
   print("z", end='')
# for blanks
  for i in range (col2):
   print("z", end="")
  col2=col2-1
  
#for star
  for i in range (col2):
   print("*", end="")
  col2=col2+1
  print("")

column=0
col2=0
for i in range (row):
  column=int(column+1)
  
# for stars
  for i in range (column):
   print("*", end='')
  print("")

