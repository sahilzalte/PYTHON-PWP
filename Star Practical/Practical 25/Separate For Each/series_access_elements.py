import pandas as pd

# Create a Series
list_data = [5, 15, 25, 35, 45]
series_from_list = pd.Series(list_data)

# 3. Access Elements of a Series
print("3. Accessing Elements from Series:")
print("First Element:", series_from_list[0])
print("Last Element:", series_from_list[len(series_from_list) - 1])
