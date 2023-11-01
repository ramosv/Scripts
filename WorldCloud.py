import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from newsapi import NewsApiClient

url = "https://newsapi.org/v2/everything?"
secret = "5c3afe7068fd42c98b4206cfa207105a"

newsapi = NewsApiClient(api_key="5c3afe7068fd42c98b4206cfa207105a")

parameters = {"q": "Chess", "pageSize": 20, "apiKey": secret}

## Making the request
response = requests.get(url, params=parameters)

# Convert the response to JSON format
response_json = response.json()

text = []

for i in range(50):
    text.append(response_json)


for i in range(len(text)):
    text_combined = ""
    for j in text[i]["articles"]:
        text_combined += j["title"] + ""

    if text_combined != "":
        cloud = WordCloud(max_font_size=40).generate(text_combined)
        plt.figure()
        plt.imshow(cloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
