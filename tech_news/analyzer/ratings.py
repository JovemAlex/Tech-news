from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    top = []
    news_filtered = search_news({})
    if news_filtered:
        [top.append(news["category"]) for news in news_filtered]
        contagem = Counter(top)
        return sorted(
            contagem.keys(),
            key=lambda categoria: (-contagem[categoria], categoria),
        )[:5]
    else:
        return []


test = top_5_categories()
print(test)
