import requests
from bs4 import BeautifulSoup
import pandas as pd
import wikipedia as wp

#Get the html source and read the 11th table on the page
html = wp.page("List of wars and anthropogenic disasters by death toll").html().encode("UTF-8")
df = pd.read_html(html)[11]

#select the first 5 rows and rename the columns
df = df[:5]

#drop the 'Notes' column and rename headers
df.drop(columns='Notes',inplace=True)
df.rename(columns={"Leader(s)": "Leader", "Lowest estimate": "Lowest_est", "Highest estimate": "Highest_est", "Geom. mean estimate[1]": "Mean_est"}, inplace=True)

#add world population data and death tolls as a share of the world population
worldpop = [1260000000, 2520000000, 400000000, 2300000000, 2070000000]
df['Worldpop'] = worldpop
df['Mean_est'] = df['Mean_est'].astype(int)
df['Worldpop_share'] = df.apply(lambda row: row.Mean_est/row.Worldpop, axis=1)

#strings cleanup

print(df)
#export to .csv
df.to_csv('deaths-per-leader.csv',header=1,index=False)
