import requests


API_KEY="###"


# Categories: business, entertainment, general, health, science, sports, technology
category = "entertainment"
country="us"
request2 = requests.get(f"https://newsapi.org/v2/top-headlines/sources?category={category}&language=en&apiKey={API_KEY}")
response2 = request2.json()
# print(response2["sources"])
source_list = []
for source in response2["sources"]:
    source_list.append(source["id"])
    source_list.append(source["url"])
# print(source_list)
general_source_ids = ["abc-news", "abc-news-au", "bbc-news", "google-news", "the-huffington-post",
                      "the-washington-post", "time"]
business_source_ids = ["bloomberg", "business-insider", "fortune", "the-wall-street-journal",
                       "australian-financial-review", "business-insider-uk", "financial-post"]
tech_source_ids = ["techcrunch", "techradar", "the-verge", "wired"]
science_source_ids = ["national-geographic"]