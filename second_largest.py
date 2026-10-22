a=[2,4,5,1,0,10,100,8]
largest=a[0]
second_largest=0  
for i in a:
  if largest<i:
    second_largest=largest
    largest=i
  elif i>second_largest and i<largest:
    second_largest=i
if second_largest == a[0]:
    print("No second-largest distinct number")
else:
    print(second_largest)    
 
  