# 1. Create a Set
my_set = {10, 20, 30, 40, 50}
print("Created Set:", my_set)

# 2. Access Set Elements (Looping, since indexing is not allowed in sets)
print("Accessing Set Elements:")
for element in my_set:
    print(element, end=" ")
print()

# 3. Update Set (Add and Remove Elements)
my_set.add(60)  # Adding a single element
print("After adding 60:", my_set)

my_set.update([70, 80, 90])  # Adding multiple elements
print("After adding multiple elements:", my_set)

my_set.remove(30)  # Removing an element (raises error if not found)
print("After removing 30:", my_set)

my_set.discard(100)  # Discarding an element (does not raise error if not found)
print("After discarding 100 (if present):", my_set)

# 4. Delete Set
my_set.clear()  # Deleting the set
print(my_set)  # This will raise an error as set is deleted