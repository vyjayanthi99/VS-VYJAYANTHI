number = "153"
length= len(number)
sum=0 
for i in number:
    sum= sum+ (int(i)** length)
if  sum == int(number):
   print("Armstrong Number")
else:
    print("Not an Armstrong Number")