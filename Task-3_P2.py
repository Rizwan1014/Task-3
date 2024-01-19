'''
Given a python list [10,501,22,37,100,999,87,351] your task is to count all the prime numbers and create a new python list which will contain all the prime number in it.
'''
# given list 
list=[10,501,22,37,100,999,87,351]
prime=[] # empty list to store prime number 
for i in list:
 c=0
 for j in range(1,i):
   if i%j==0:
    c+=1
 if c==1:
  prime.append(i)
  #print the prime number from the list 
  print("The list of number is :",list)
  print("The prime number is :",prime)
        

    
