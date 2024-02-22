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


def index(request, category="nation"):
    apikey = s.NEWS_API_KEY
    category = category
    url = f"{s.NEWS_HOST}?category={category}&lang={s.NEWS_LANG}&country={s.NEWS_COUNTRY}&max=10&apikey={apikey}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

    return render(request, "news/index.html", {"articles": articles, "categories": categories})
