arr = [1,2,3,3,4,5,5]
finalarr=[]
for i in arr :
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)