start=int(input("Enter start time: "))
finish=int(input("Enter finish time: "))

if start>finish:
  print("Error, start is bigger than finish") #2.4
  buffer=finish
  finish=start
  start=buffer
  
for counter in range (start,finish+1):
 print(start)
 start=start+1
 