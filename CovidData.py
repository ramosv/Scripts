from bs4 import BeautifulSoup
import requests
import json
from prettytable import PrettyTable

covidSite = "https://cdphe.colorado.gov/covid-19/data"

covid = requests.get(covidSite)
covidData = BeautifulSoup(covid.text, "html.parser")

table = covidData.find_all('table',attrs={'dir':'ltr'} )
rows = covidData.find_all('tr')


print(len(table), "tables found.")
print(len(rows), "rows found.")



data = []

## Create a dictionary with the data.
index = 0

while index < len(rows):
    temp = []
    for td in rows[index].find_all('td'):
        temp.append(td.text.replace('\n', ' ').strip())
    data.append(temp)
    index +=1
    print(temp)

countyData = []

for i in data:
    if len(i) > 2:
        countyData.append(i)



print(len(countyData), "county data entries found.")

print(countyData[:2])  # Print first 2 entries of countyData for checking

county = PrettyTable(["County","Cases","Deaths Due to COVID-19"])
idx = 0

print(county)


#County Table
for x in countyData:
    row = [x[0],x[1],x[2]]
    if len(row) == 3:
        county.add_row(row)
    else:
        print(f"A row was skipped: {row}")
    

show_county_html = open("countyCovid.html", 'w')

show_county_html.write(
    county.get_html_string(
        attributes={
            "id": "Covid Data",
            "class": "table",
            "border": 2,
            "style": "padding: 5px; background-color:#f0f8ff"
        }))
