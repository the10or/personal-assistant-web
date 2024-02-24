import json
import urllib.request

from django.conf import settings as s
from django.shortcuts import render

categories = [
    "general",
    "world",
    "nation",
    "business",
    "technology",
    "entertainment",
    "sports",
    "science",
    "health"
]

def mock_json_response():
    # Return a static JSON response here
    return {
        "articles": [
            {"title": "Article 1", "content": "Content 1"},
            {"title": "Article 2", "content": "Content 2"}
        ]
    }
def index(request, category="nation"):
    apikey = s.NEWS_API_KEY
    category = category
    host = s.NEWS_HOST
    lang = s.NEWS_LANG
    country = s.NEWS_COUNTRY

    # url = f"{host}?category={category}&lang={lang}&country={country}&max=10&apikey={apikey}"
    # with urllib.request.urlopen(url) as response:
    #     data = json.loads(response.read().decode("utf-8"))
    #     articles = data["articles"]

    articles = mock_json_response()["articles"]

    return render(request, "news/index.html", {"articles": articles, "categories": categories})
