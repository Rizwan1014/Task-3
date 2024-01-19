'''
Given a Python list[10,501,22,37,100,999,87,351] .Find out how many numbers are there in the given Python list which are Happy Numbers?
'''
# list is the given data , list1 is the empty list to store 
list = [10,501,22,37,100,999,87,351]
list1 = []
def is_happy(list):
    for i in range (len(list)):
        sum = list[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            list1.append(list[i])
    return list1
print(is_happy(list))
