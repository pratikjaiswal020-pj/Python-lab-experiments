#'''write a pandas program to craete a  DataFrame from a dictionary and then transpose it, ensuring that data types remain consistent.'''
import pandas as pd
#create dictionary
data ={
    'A':[1,2,3],
    'B':[4,5,6]
}
df = pd.DataFrame(data)
#transpose DataFrame 
#df_T = df.transpose()
df_T= df.T
print("original dataframe:")
print(df)
print("transposed dataframe:")
print(df_T)