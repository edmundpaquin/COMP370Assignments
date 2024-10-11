import requests
from datetime import datetime, timedelta

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    if news_keywords == []:
        raise ValueError
    for key in news_keywords:
        if not key.isalpha():
            raise ValueError
    date = datetime.now()
    past_date = date - timedelta(days=lookback_days)
    past_date_str = past_date.strftime('%Y-%m-%d')
    q = 'q=' + ' OR '.join(news_keywords)
    url = "https://newsapi.org/v2/everything?" + q + '&from=' + past_date_str + '&apiKey=' + api_key

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        articles = data.get('articles', [])
        
        return articles

    else:
        print(f"Failed to fetch articles: {response.status_code}")



if __name__ == '__main__':
    apikey = '984f1995d4ee42279c3518dbccb447e2'
    keywords = ['bamping', 'RFK', 'Israel']
    print(fetch_latest_news(apikey, keywords, 10))
