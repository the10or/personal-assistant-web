from django.shortcuts import render

# Create your views here.
import json
import random
import urllib.request
from pprint import pprint

from django.shortcuts import render

categories = ["general", "world", "nation", "business", "technology", "entertainment", "sports", "science", "health"]


# Create your views here.
def index(request, category="nation"):
    apikey = "8fa3ab2e35deefffc7007a3cc701766c"
    category = category
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=uk&country=ua&max=10&apikey={apikey}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
        articles_on_page = []
        for i in range(3):
            ind = random.randint(0, len(articles) - 1)
            article = articles[ind]
            articles_on_page.append(article)


    return render(request, "news/index.html", {"articles": articles_on_page, "categories": categories})
