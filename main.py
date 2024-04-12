# Pandas TypeError: no numeric data to plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'year': [2011, 2014, 2018, 2012, 2025],
    'net_worth': ['5000', '10000', '15000', '10000', '20000'],
    'gdp_per_capita': ['10000', '12000', '15000', '20000', '25000'],
})

df = df.astype(float)

print(df[['net_worth', 'gdp_per_capita']].plot())

plt.show()