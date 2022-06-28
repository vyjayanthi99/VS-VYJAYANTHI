# write a program to read text.file 

file1 = open("test.txt","r")
data=file1.read()
print(data)
print()

file2 =open("blank.txt","w")
str1 = "addition"
file2.write(str1)
print()

file3 = open("testtxt","r+")
print(file3.readline(11))
print()