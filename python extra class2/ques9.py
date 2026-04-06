#'''write a pandas program to split the following dataframe into groups based on school code. also check the type of GroupBy object.'''
import pandas as pd
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_column',None)
student_data=pd.DataFrame({
    'school_code': ['S1', 'S1', 'S2', 'S2', 'S3'],
    'student_name': ['Ram', 'Shyam', 'Amit', 'John', 'Riya'],
    'marks': [85, 90, 78, 88, 92]
})

df = pd.DataFrame(student_data)

print("Original DataFrame:\n")
print(df)

# Step 2: Group by 'school_code'
grouped = df.groupby('school_code')

# Step 3: Check type of GroupBy object
print("\nType of grouped object:")
print(type(grouped))

# Step 4: Display each group
print("\nGrouped Data:\n")
for school_code, group in grouped:
    print(f"School Code: {school_code}")
    print(group)
    print("-" * 30)
