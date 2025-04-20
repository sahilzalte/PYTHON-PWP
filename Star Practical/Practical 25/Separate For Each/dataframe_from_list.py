import pandas as pd

# Create DataFrame from a List
data_list = [['John', 28, 'San Francisco'], ['Emma', 22, 'Boston'], ['Liam', 31, 'Seattle']]
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("DataFrame from List:\n", df_from_list)



# This is made by me 

data_list2 = [['sai',25,'visapur'], ['aman',18,'yeola']]
dataframe_from_list2 = pd.DataFrame(data_list2, columns=['Name', 'Age', 'City'])
print("DataFrame from List2:\n", dataframe_from_list2)