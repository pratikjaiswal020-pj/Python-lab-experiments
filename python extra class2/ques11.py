#''' write a pandas program to draw a basic line plot with pandas and matplotlib
# create a sampe dataframe with year and sakes coloums
# use plt.plot()to plot year vs sales
# add axis labels and a title to the using plt.xlabels(), plt.ylabel() and plt.title()
# display thr plot using pllt.show().'''
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [100, 150, 130, 170, 200]
}

df = pd.DataFrame(data)
plt.plot(df['year'], df['sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Year vs Sales Line Plot')
plt.show()