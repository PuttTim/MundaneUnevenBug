row=int(input("Enter row number here: "))
if row<3:
  print("error, setting input to 3")
  row=3
column=row
col2=1

for i in range (row):
  



# for blanks

  for ii in range (column):
    print(" ", end='')
  column=int(column-1)
  
# for stars 
  n=i-1
  col2=3+2*n
  for i in range (col2):
    print("*", end='')
    
  print("")



# for bottom half


n=row-1
col4=3+2*n
col3=row-row
for i in range (row+1):

# for blanks


  for i in range (col3):
    print(" ", end="")
  col3=col3+1  
  
  

# for stars 
  
  
  for j in range (col4):
    print("*", end='')
  col4=col4-2
  
  
  print("")

