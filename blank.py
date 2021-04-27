row=int(input("Enter row number here: "))
column=row
for i in range (row):
  column=int(column-1)
  for i in range (column):
   print("=", end='')
  print('')