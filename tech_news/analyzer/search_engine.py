from tech_news.database import db
import re
from datetime import datetime


def search_by_title(title):
    insensitive_pattern = re.compile(title, re.IGNORECASE)

    news_list = [
        (news["title"], news["url"])
        for news in db.news.find({"title": insensitive_pattern})
    ]

    return news_list


def search_by_date(date):
    try:
        formated_date = (
            datetime
            .strptime(date, "%Y-%m-%d")  # converts string to date
            .strftime("%d/%m/%Y")  # convert date to format dd/mm/AAAA
        )
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_list = [
            (news["title"], news["url"])
            for news in db.news.find({"timestamp": formated_date})
        ]
        return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
