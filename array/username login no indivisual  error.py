num=int(input("Enter amount of users here: "))
login=[[0 for i in range(num)] for i in range (2)]
#print(login)

for x in range(num):
  for i in range(0,2,num):
    username=input("Username: ")
    
    login[i][x]=username
    #print("i", i, ", x", x)
  for j in range(1,2,num):
    password=input("Password: ")  
    login[j][x]=password
    #print("j", j, ", x", x)
  
#print(login)

o=0
p=0
#print(login[o][p], login[o+1][p])
#print("O: ", o, "P: ", p)

us=""

ul=input("Username login:")
pl=input("Password login:")
#print(ul, pl)

for e in range (num):
  for w in range(num):
    for q in range(num):
      #print("Q:", q, "W:", w)
      if ul == login[w][q] and pl == login[e][q]:
        us=("success")     
    
      else:
        uf="error"
        
      #print(login[w][q])
      #print(login[e][q])

if us == "success":
  print(us)
else:print(uf)


  