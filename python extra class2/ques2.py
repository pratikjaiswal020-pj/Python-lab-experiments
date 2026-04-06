import pandas as pd 
s= pd.Series(['2023-01-01','not a date','2024-05-10'])
#convert to datetime
dt_s = pd.to_datetime(s,errors='coerce')
#values-------> converted to NaT(Not a Time)
#Filter valid dates like nan or nat'
valid_dates= dt_s.dropna()
print(valid_dates)