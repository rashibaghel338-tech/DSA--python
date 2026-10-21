num =int(input("enter a num:"))
total=0
ld=0
c=num
digits = len(str(num))
while num>0:
  ld=num%10
  total+=ld** digits
  num=num//10
  
if total==c:
  print("armstrong")
else:
  print("not")
