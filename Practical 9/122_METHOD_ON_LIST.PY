# 1. Create a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Created Tuple:", my_tuple)

# 2. Access Tuple elements (Indexing)
print("Accessing first element:", my_tuple[0])  # Accessing first element

# 3. Print the entire Tuple
print("Printing Tuple:", my_tuple)

# 4. Delete the Tuple (Tuples are immutable, so we delete the whole tuple)
del my_tuple
print(my_tuple)  # This will raise an error as tuple is deleted


# 5. Convert Tuple into List and Vice-Versa
tuple_data = (1, 2, 3, 4, 5)  # Original Tuple
list_data = list(tuple_data)  # Convert tuple to list
print("Converted Tuple to List:", list_data)

tuple_again = tuple(list_data)  # Convert list back to tuple
print("Converted List back to Tuple:", tuple_again)

