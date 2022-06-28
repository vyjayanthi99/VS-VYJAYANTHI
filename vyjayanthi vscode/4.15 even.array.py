arr = [1,2,3,4,5,6,7,9]
evennumbers=0 
oddnumbers=0
for i in arr:
    if i%2==0:
        evennumbers+=1
    else:
        oddnumbers+= 1
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)
        