import pandas as pd
import numpy as np  # For creating an array

# 1. Create Series from a NumPy Array
array_data = np.array([10, 20, 30, 40, 50])
series_from_array = pd.Series(array_data)
print("1. Series from NumPy Array:\n", series_from_array)

print("\n------------------------------\n")

# 2. Create Series from a List
list_data = [5, 15, 25, 35, 45]
series_from_list = pd.Series(list_data)
print("2. Series from List:\n", series_from_list)

print("\n------------------------------\n")

# 3. Access Elements of a Series
print("3. Accessing Elements from Series:")
print("First Element:", series_from_list[0])
print("Last Element:", series_from_list.iloc[-1])

print("\n------------------------------\n")

# 4. Create DataFrame using List or Dictionary
# Creating DataFrame from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_from_dict = pd.DataFrame(data)
print("4. DataFrame from Dictionary:\n", df_from_dict)

print("\n------------------------------\n")

# Creating DataFrame from a List
data_list = [['John', 28, 'San Francisco'], ['Emma', 22, 'Boston'], ['Liam', 31, 'Seattle']]
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("DataFrame from List:\n", df_from_list)
