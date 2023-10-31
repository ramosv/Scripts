from bs4 import BeautifulSoup
import requests
import json
from prettytable import PrettyTable


#Send a http get request to website and return contents of the page in results
website = "http://www.ucdenver.edu/pages/ucdwelcomepage.aspx"
site = requests.get(website)

soup = BeautifulSoup(site.text, "html.parser")

data = json.loads(soup.find("script", type="application/ld+json").string)

tempDictonary = {}
list_dictionary = []
display = PrettyTable(["Name","Telephone","Email","URL"])

## Create a list of dictionaries with the json data.
for d in data["department"]:
    tempDictonary = {}
    tempDictonary["name"] = d.get("name")
    tempDictonary["telephone"] = d.get("telephone")
    tempDictonary["email"] = d.get("email")
    tempDictonary["url"] = d.get("url")

    display.add_row([d.get("name"),d.get("telephone"),d.get("email"),d.get("url")]) 
    list_dictionary.append(tempDictonary)


with open('dataFromSite', 'w') as file:
   json.dump(list_dictionary, file, indent=4)


# HTML Output
show_in_html = open("departments.html", 'w')

show_in_html.write(
    display.get_html_string(
        attributes={
            "id": "Departments",
            "class": "table",
            "border": 2,
            "style": "padding: 5px; background-color:#f0f8ff"
        }))