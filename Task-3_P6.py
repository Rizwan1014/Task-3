'''
You have been three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?
'''
def find_duplicates(list1, list2, list3):
    # Concatenate the three lists into a single list
    combined_list = list1 + list2 + list3

    # Create a dictionary to count the occurrences of each element
    element_count = {}
    duplicate = set()

    # Iterate through the combined list
    for element in combined_list:
        if element in element_count:
            duplicate.add(element)
        else:
            element_count[element] = 1

    return list(duplicate)

# Three list are 
print("The List are :")
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
# duplicate list are stored in result 
result = find_duplicates(list1, list2, list3)
# to dispaly ouput 
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Duplicate:", result)
