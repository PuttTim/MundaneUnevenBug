num1=int(input("Number of student here:"))

name=[0 for i in range(num1)]
score=[0 for j in range(num1)]
grade=["Error" for k in range(num1)]



for i in range(num1):
  name[i]=input("Enter name here:")
  
  si=(int(input("Enter score here:")))
  if si<0 or si>100:
    si2=(int(input("Error: Enter another score, no minuses:")))
    
    if si2<0 or si2>100:
      print("Error: Setting score to 0 for", name[i])
      si3=0
      score[i]=si3
      gi=0
    else:
      score[i]=si2
      gi=si2
  else:
    score[i]=si
    gi=si
  
  
  
  
  if gi <= 100 and gi >= 80:
    gf="A"
  elif gi<80 and gi>=60:
    gf="B"
  elif gi<60 and gi>=40:
    gf="C"
  elif gi<40 and gi>=20:
    gf="D"
  else:
    gf="F"
  

    



  
  grade[i]=gf
print(name)
print(score)
print(grade)

