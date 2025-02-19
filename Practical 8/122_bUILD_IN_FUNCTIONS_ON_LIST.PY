# Creating a sample list
numbers = [5, 2, 9, 1, 5, 6]

# 1. append(): 
numbers.append(10)
print("After append(10):", numbers)

# 2. insert(): 
numbers.insert(2, 15)  
print("After insert(2, 15):", numbers)

# 3. remove(): 
numbers.remove(5)  
print("After remove(5):", numbers)

# 4. pop(): 
popped_element = numbers.pop()
print("After pop():", numbers, "Popped element:", popped_element)

# 5. sort(): 
numbers.sort()
print("After sort():", numbers)

# 6. reverse(): 
numbers.reverse()
print("After reverse():", numbers)

# 7. count(): 
count_five = numbers.count(5)
print("Count of 5:", count_five)

# 8. index(): 
index_six = numbers.index(6)  
print("Index of 6:", index_six)