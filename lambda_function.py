import requests
from bs4 import BeautifulSoup
import pandas as pd

website_url = requests.get("https://en.wikipedia.org/wiki/List_of_wars_and_anthropogenic_disasters_by_death_toll#List_of_political_leaders_and_regimes_by_death_toll").text

soup = BeautifulSoup(website_url,"lxml")
print(soup.prettify())

My_table = soup.find('table',{'class':'sortable wikitable'})
print(My_table)

links = My_table.findAll('a')
print(links)

Countries = []
for link in links:
    Countries.append(link.get('title'))
    
print(Countries)

df = pd.DataFrame()
df['Country'] = Countries

print(df)


# import json
# from datetime import datetime
# import os
# import boto3
# from craigslist import CraigslistHousing

# def lambda_handler(event, context):

# 	# Pull in environmental variable for number of posts to pull
# 	number_of_posts = os.environ.get("number_of_posts")

# 	# Instantiate our Craigslist scraper
# 	cl = CraigslistHousing(site='newyork', 
# 							area=None, 
# 							category='aap')

# 	# Pull data from Craigslist and put into a list
# 	results = cl.get_results(sort_by='newest', geotagged=True, limit=5)
# 	resultsList = [result for result in results]
	
# 	# Convert data to json
# 	data = json.dumps(resultsList)

# 	# Get the current datetime for the file name
# 	now = str(datetime.today())
	
# 	# Export the data to S3
# 	client = boto3.client('s3')
# 	response = client.put_object(Bucket='lazyapartment', 
# 					Body=data, 
# 					Key='rawdata/{}.json'.format(now))