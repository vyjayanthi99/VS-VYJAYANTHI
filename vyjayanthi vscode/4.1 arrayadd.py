# write a function to add integer values of an array

from audioop import avg 
from operator import index 
from turtle import position 
from typing import final

#Initializing array 
arr = [10,20,30,40]
sum=0
# loop through the array to calclate sum of elements 
for i in range(0,len(arr)):
    sum = sum+arr[i]
print("sum of all integer values in array:",sum)