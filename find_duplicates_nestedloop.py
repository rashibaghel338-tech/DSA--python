a=[1,2,3,45,2,6,8,0,3,1]
duplicates=[]
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if a[i]==a[j] and a[i] not in duplicates:
      duplicates.append(a[i])
print(duplicates)      

    