arr = [10,20,30,40]
def cal_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num+i 
        avg = sum_num/len(num)
        return avg 
print("The average is",cal_average([10,21,32,43,54]))

