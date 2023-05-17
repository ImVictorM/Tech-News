from tech_news.database import db
import re


def search_by_title(title):
    insensitive_pattern = re.compile(title, re.IGNORECASE)

    news_list = [
        (news["title"], news["url"])
        for news in db.news.find({"title": insensitive_pattern})
    ]

    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
