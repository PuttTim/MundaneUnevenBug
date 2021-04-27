row=int(input("Enter row number here: "))
column=0
col2=0
empty=row
for i in range (row):
  column=int(column+1)
  empty=int(empty-1)
# for stars
  for i in range (column):
   print("*", end='')
   
  for i in range (empty):
   print("z", end='')
  print("")
