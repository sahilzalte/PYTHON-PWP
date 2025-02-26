# 1. Create a Dictionary
my_dict = {
    "name": "Sahil",
    "age": 18,
    "city": "Yeola"
}
print("Initial dictionary:", my_dict)

print()
# 2. Access Dictionary
print("Access name:", my_dict["name"])


print()
# 3. Update Dictionary
my_dict["age"] = 31
print("Updated age:", my_dict["age"])


print()
# 4. Delete Dictionary
del my_dict["city"]
print("Dictionary after deleting city:", my_dict)


print()
# 5. Looping Through Dictionary
print("\nLooping through keys:")
for key in my_dict:
    print(key, "->", my_dict[key])


print()
# 6. Create Dictionary From List

keys_list = ["apple", "banana", "cherry"]
# We can create a dictionary with a default value (e.g., 0)
fruits_dict = dict.fromkeys(keys_list, 0)
print("Dictionary created from list:", fruits_dict)

