a=[1,2,3,45,2,6,8,0,3,1]
duplicates=[]
for i in a:
  if a.count(i)>1 and i not in duplicates:
    duplicates.append(i)
print(duplicates)    
