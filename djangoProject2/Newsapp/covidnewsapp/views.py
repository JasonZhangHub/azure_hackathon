from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key='3002a7015bd143c48157daa21b02e0ce')
    headLines = newsApi.get_top_headlines(q='COVID',sources='cnn,bbc-news')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})

