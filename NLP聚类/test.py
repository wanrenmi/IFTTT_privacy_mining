import pandas as pd
csv_file = "tweet1.csv"
column_name = "username"
df = pd.read_csv(csv_file)
username = df.iloc[:,7]
print(type(username[1]))
