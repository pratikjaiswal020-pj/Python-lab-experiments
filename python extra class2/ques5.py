import pandas as pd
s= pd.Series(['apple','banana','apple','orange'])
p= pd.Series(['lion','cat','dog','tiger','monkey','dog','cat'])
#convert to categorical
cat_s = s.astype('category')
print(cat_s)
animal = p.astype('category')
print(animal)
#Display category codes
print(cat_s.cat.codes)
print(animal.cat.codes)
