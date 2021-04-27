num1=int(input("Number of student here:"))

name=[0 for i in range(num1)]
score=["Error" for j in range(num1)]
grade=["Error" for k in range(num1)]



for i in range(num1):
  name[i]=input("Enter name here:")
  
  si1=(int(input("Enter score here:")))
  
  if si1 > 100 or si1 < 0:
    si2="Error"
    gi=si1
    score[i]=si2
  else:score[i]=si1
  gi=si1
  
  
  
  if gi<=100 and gi>=80:
    gf="A"
  elif gi<80 and gi>=60:
    gf="B"
  elif gi<60 and gi>=40:
    gf="C"
  elif gi<40 and gi>=20:
    gf="D"
  elif gi<20 and gi>=0:
    gf="F"
  else:
    gf="Error"
    



  
  grade[i]=gf
print(name)
print(score)
print(grade)

