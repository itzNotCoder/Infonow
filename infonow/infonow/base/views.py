from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def espn_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='espn')
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

    return render(request, 'espn-news.html', context={"mylist": mylist})

def ign_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='ign')
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

    return render(request, 'ign-news.html', context={"mylist": mylist})

def cnn_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='cnn')
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

    return render(request, 'cnn-news.html', context={"mylist": mylist})

def bbc_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='bbc-news')
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

    return render(request, 'bbc-news.html', context={"mylist": mylist})

def theverge_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='the-verge')
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

    return render(request, 'theverge-news.html', context={"mylist": mylist})

def techcrunch_news(request):
    newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
    headLines = newsApi.get_top_headlines(sources='techcrunch')
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

    return render(request, 'techcrunch-news.html', context={"mylist": mylist})

# def football_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='football', domains='espn.com', from_param='2022-12-02', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'football-news.html', context={"mylist": mylist})

# def basketball_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='basketball', domains='espn.com', from_param='2022-12-02', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'basketball-news.html', context={"mylist": mylist})

# def baseball_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='baseball', domains='espn.com', from_param='2022-12-02', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'baseball-news.html', context={"mylist": mylist})

# def cricket_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='cricket', domains='espncricinfo.com', from_param='2022-12-01', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'cricket-news.html', context={"mylist": mylist})

# def bitcoin_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='crypto', domains='bbc.com, cnn.com, sky.com', from_param='2022-12-01', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'bitcoin-news.html', context={"mylist": mylist})

# def coronavirus_news(request):
#     newsApi = NewsApiClient(api_key='e53e38b7b0df49b7bfcf7c6d35123458')
#     headLines = newsApi.get_everything(q='coronavirus', domains='bbc.com, cnn.com', from_param='2022-12-01', to='2022-12-04', language='en', sort_by='relevancy')
#     articles = headLines['articles']
#     desc = []
#     news = []
#     img = []

#     for i in range(len(articles)):
#         article = articles[i]
#         desc.append(article['description'])
#         news.append(article['title'])
#         img.append(article['urlToImage'])
#     mylist = zip(news, desc, img)

#     return render(request, 'coronavirus-news.html', context={"mylist": mylist})

def aboutus(request):
    return render(request, 'about-us.html')

def contactus(request):
    # if request.method == 'POST':
    #     message = request.POST['message']
    #     send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['muhammadabdulsalam757@gmail.com'], fail_silently=False)
    return render(request, 'contact-us.html')
