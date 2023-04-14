from tech_news.database import search_news
# from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_filtered = search_news({"title": {"$regex": title, "$options": "i"}})
    if news_filtered:
        return [(news["title"], news["url"]) for news in news_filtered]
    else:
        return []


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
