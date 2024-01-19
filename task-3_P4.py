'''
Write a python program o find the sum of the first and last digit of an integer?
'''
# declare number 
number = 1456
# type casting it in string
number= str(number)
first_num= int(number[0])
last_num= int(number[-1])
#addition of 2 num
add = first_num + last_num
# display the result
print('Sum of fist and last num: ',add)
