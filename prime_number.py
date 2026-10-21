num=int(input("enter a num:"))
total=0
for i in range(1,num+1):
  if num%i==0:
    total+=1
if total==2:
  print("prime")
else:
  print("not prime")