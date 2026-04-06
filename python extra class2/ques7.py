#'''write a pandas program to create a dataframe from a dictionary whre values are lists of unequal by lengthts by filling missing values with none.'''
import pandas as pd
data = {
    'A':[1,2,3],
    'B':[4,5],
    'C': [6,7,8,9]
}
df= pd.DataFrame(dict([(k,pd.Series(v)) for k , v in data.items()]))
df = df.where(pd.notnull(df),None)
print(df)