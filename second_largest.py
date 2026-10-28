a = [5,5,5]
lar_num = a[0]
sec_num = float('-inf')

for i in range(len(a)):
    if a[i] > lar_num:
        sec_num = lar_num
        lar_num = a[i]

    elif a[i] < lar_num and a[i] > sec_num:
        sec_num = a[i]
if sec_num == float('-inf'):
    print("No second-largest distinct number")
else:
    print("Second largest:", sec_num)      

print("Largest:", lar_num)














