arr = [1,1,4,5,5,6]
for i in range(0,len(arr)):
    for k in range(i+1,len(arr)):
        if arr[i]==arr[k]:
            print("Duplicate element in given array:",arr[k])