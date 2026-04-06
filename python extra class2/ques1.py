import pandas as pd
s= pd.Series(['10','20','abc','30'])
numeric_s = pd.to_numeric(s,errors='coerce')
print(numeric_s)

#converts values to int or float
#tries to inerpret each string as a number
#note:error='coerce'
# this is the key concept if the conversion is possible then it converts normally, if conversion fails then it replaces with NaN(Not a Number)