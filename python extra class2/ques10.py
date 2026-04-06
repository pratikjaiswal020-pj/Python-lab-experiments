#'''write a pandas program to merge two DataFrame on a single column id.
import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Ram', 'Shyam', 'Amit', 'John']
})
df2 = pd.DataFrame({
    'id': [1, 2, 3, 5],
    'marks': [85, 90, 78, 88]
})
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
merged_df = pd.merge(df1, df2, on='id')
print("\nMerged DataFrame:\n", merged_df)