import urllib.request,json
from .models import News,Articles


# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
def process_results(news_list):
    '''
    Function that processes the news results and transform them to list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
        Return:
        news_results: Alist of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        
        news_object = News(id,name,description,url,category)
        news_results.append(news_object)
    return news_results
def get_articles(id):
    get_new_details_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        if news_details_response ['articles']:
            news_details_response_data = news_details_response['articles']
            news_articles = process_articles(news_details_response_data)

    return news_articles
        
def process_articles(articles_list):        
    
    '''
    Function that processes the articles results and transform them to list of Objects      
    Args:
        articles_list: A list of dictionaries that contain news details
        Return:
        articles_results: A list of news objects
    '''
    articles = []
    for news_details_response in articles_list:
        if news_details_response:
            id = news_details_response.get('id')
            image = news_details_response.get('urlToImage')
            description = news_details_response.get('description')
            articlesSource = news_details_response.get('url')
            timePublished = news_details_response.get('publishedAt')
            author = news_details_response.get('author')

            news_object = Articles(id,image,description,articlesSource,timePublished,author)
            articles.append(news_object)

    return articles
