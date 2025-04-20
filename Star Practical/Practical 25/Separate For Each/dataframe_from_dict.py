import pandas as pd


dict_data = {
    'name' : ['aman','ram','shyam'],
    'age' : [25, 18, 30],
    'city' : ['visapur','yeola','vikharni']
}

dataframe_from_dict  = pd.DataFrame(dict_data)
print(dataframe_from_dict)