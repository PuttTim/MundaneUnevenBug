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


# col4=row+row-1
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
  for i in range (col4+2):
    print("K", end='')
    col4=col4-3
  print("")







# H.W. do bottom half of diamond, using for i in range(start, finish, how much per increments(-1, 2, 3, ...))

# 11 9 7 5 3 1
# 1  2 3 4 5 6
# Input = 6