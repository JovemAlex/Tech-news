import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if request.status_code == 200:
            return request.text
        if not request.status_code == 200:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    news = []
    selector = Selector(text=html_content)
    news = selector.css(".entry-title a::attr(href)").getall()
    if news:
        return news
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    new_page = selector.css(".next::attr(href)").get()
    if new_page:
        return new_page
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
