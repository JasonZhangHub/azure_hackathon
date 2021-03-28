from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
###Remove API key for security reason can apply for a personal one on newsapi

def index(request):
    newsApi = NewsApiClient(api_key='')
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

