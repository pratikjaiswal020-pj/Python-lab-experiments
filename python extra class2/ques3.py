import pandas as pd
s= pd.Series(['1,000','2,500','3,750'])
#remove commas and convert it into float
float_s = s.str.replace(',',"").astype(float)
print(float_s)
                        