import requests
from sys import argv
from dotenv import load_dotenv
import os

load_dotenv()

APIKey = os.getenv("APIKEY")
URL = 'https://newsapi.org/v2/top-headlines'


def get_by_category(category):
    query_parameters = {
        "apiKey": APIKey,
        "category": category,
        "language": "en",
        "country": "us"
    }
    get_articles(query_parameters)


def get_by_query(query):
    query_parameters = {
        "q": query,
        "apiKey": APIKey,
        "language": "en",
        "country": "us"
    }
    get_articles(query_parameters)


def get_articles(params):
    response = requests.get(URL, params=params)
    
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return

    data = response.json()
    articles = data.get('articles', [])

    for article in articles:
        print(article.get("title"))
        print(article.get("url"))
        print() 


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script.py <category>")
    else:
        print(f"Getting news for category: {argv[1]}...\n")
        get_by_category(argv[1])
        print("\nAlso fetching news for: 'Liz Truss'\n")
        get_by_query("Liz Truss")
        
#python3 news.py technology
