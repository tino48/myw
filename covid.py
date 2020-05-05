import pycountry
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
print(df1.head(3))  # Get first 3 entries in the dataframe
print(df1.tail(3))  # Get last 3 entries in the dataframe
#### ----- Step 2 (Select data for Switzerland)----
df_CH = df1[df1['Country'] == 'Switzerland']
print(df_CH.tail(20))
#### ----- Step 3 (Plot data)----
# Increase size of plot
plt.rcParams["figure.figsize"]=20,20  # Remove if not on Jupyter
# Plot column 'Confirmed'
df_CH.plot(kind = 'line', x = 'Date', y = 'Confirmed', color = 'blue', title = 'Schweiz')

ax1 = plt.gca()
df_CH.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
plt.show()

