'''
You have given a Python List[10,501,22,37,100,999,87,351] your task is to create two list one which have all Even Numbers and another list with all ODD numbers in it ? 


'''
# declare the given list
list=[10,501,22,37,100,999,87,351]
#create empty list to store even and odd numbers from the given list 
listEven=[]
listOdd=[]
# check and append even and odd number in list
for given_num in list:
    if given_num % 2==0:# checks whether the condition is true store even number in the list 
        listEven.append(given_num)
    else:# if its false store the odd number in the list 
        listOdd.append(given_num)
#print the given list
print("The given data in the list: ",list)

#print the even and odd from the given list
print("The Even number from the given list :",listEven)
print("The Odd numbers from the given list :",listOdd)

