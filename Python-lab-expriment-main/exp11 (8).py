
import pandas as pd
df_csv = pd.read_csv('sample.csv') 
print("DataFrame from CSV:")
print(df_csv)
df_json = pd.read_json('sample.json') 
print("\nDataFrame from JSON:")
print(df_json)