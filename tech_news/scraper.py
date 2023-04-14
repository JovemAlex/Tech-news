import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".url.fn.n::text").get()
    reading_time = selector.css(".meta-reading-time::text").get().split()[0]
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
    ).strip()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    blog = "https://blog.betrybe.com/"
    news_url = []
    content = fetch(blog)

    while len(news_url) < amount:
        news_url += scrape_updates(content)
        content = fetch(scrape_next_page_link(content))

    news_content = [scrape_news(fetch(new)) for new in news_url[:amount]]
    create_news(news_content)
    return news_content
