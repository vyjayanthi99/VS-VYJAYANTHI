try:
    a = 5 
    b = 0 
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Denominator can't be zero")

m = [1,2,3]
n= [3,2,1]
try:
     m == n
except:
    print("they are not equal")
else:
    print("both equal")

s =[5,4,7]
try:
    print("second element :".s[1])
    print("fouth element:".s[3])
except:
    print("An error occured ")

    