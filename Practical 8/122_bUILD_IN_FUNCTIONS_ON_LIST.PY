# Define a list
my_list = [3, 1, 4, 1, 5, 9, 2]

# 1. Get length of list
print("1. Length of list:", len(my_list))

# 2. Find max value in list
print("2. Max value:", max(my_list))

# 3. Convert tuple to list
my_tuple = (10, 20, 30)
new_list = list(my_tuple)
print("3. Converted list:", new_list)

# 4. Append element to list
my_list.append(6)
print("4. After append:", my_list)

# 5. Count occurrences of an element
print("5. Count of 1:", my_list.count(1))

# 6. Extend list with another list
my_list.extend([7, 8, 9])
print("6. After extend:", my_list)

# 7. Insert element at specific index
my_list.insert(2, 100)
print("7. After insert:", my_list)

# 8. Pop last element (remove and return it)
popped_element = my_list.pop()
print("8. Popped element:", popped_element)
print("8. After pop:", my_list)

# 9. Remove first occurrence of a value
my_list.remove(1)
print("9. After remove:", my_list)
