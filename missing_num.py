a=[1,2,3,5,6,7]

actual_sum=0
for i in range(len(a)):
  actual_sum+=a[i]
n=len(a)+1  
total = n* (n+ 1) // 2
print("missing num is:",total-actual_sum)