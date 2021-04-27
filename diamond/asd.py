row=int(input("Enter row number here: "))
if row<3:
  print("error, setting input to 3")
  row=3
column=row
col2=1

for i in range (row):
  



# for blanks

  for ii in range (column):
    print("x", end='')
  column=int(column-1)
  
# for stars 
  n=i-1
  col2=3+2*n
  for i in range (col2):
    print("*", end='')
    
  print("")



# for bottom half



col4=row*n
col3=0
for i in range (row):

# for blanks


  for i in range (col3):
    print("z", end="")
  col3=col3+1  
  
  

# for stars 
  col4=row+row-1
  col5=1
  for i in range (col4+1):
    print("*", end='')
    col4=col4-1
  print("")



