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


def convert_date(date_string):
    try:
        formatted_date = (
            datetime
            .strptime(date_string, "%Y-%m-%d")  # converts string to date
            .strftime("%d/%m/%Y")  # converts date to format dd/mm/AAAA
        )
        return formatted_date
    except ValueError:
        raise ValueError("Data inválida")


def search_by_date(date):
    formatted_date = convert_date(date)

    news_list = [
        (news["title"], news["url"])
        for news in db.news.find({"timestamp": formatted_date})
    ]

    return news_list


def search_by_category(category):
    insensitive_pattern = re.compile(category, re.IGNORECASE)

    news_list = [
        (news["title"], news["url"])
        for news in db.news.find({"category": insensitive_pattern})
    ]

    return news_list
