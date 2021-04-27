login=[[0 for i in range(2)]for a in range(2)]

print(login)


for e in range(2):

    
  login[0][e]=input("Enter username here: ")
    
  login[1][e]=input("Enter password here: ")
  
  #print("loop e:", login) 
print(login)

user=input("Enter username here: ")
passw=input("Enter password here: ")

for b in range(2):
  if login[0][b] == user:
    output=2
    p=b
    break
  elif login[0][b] != user and login[1][b] != passw:
    output=0
  
if output == 2:
  if login[1][p] == passw:
    output=1
  else:
    output=3


if output == 1:
  outcome="Success"
elif output == 3:
  outcome="Incorrect password"
elif output == 0:
  outcome="Not found"



    

print(outcome)