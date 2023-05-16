import requests
from requests.exceptions import ReadTimeout
from time import sleep
from parsel import Selector


def fetch(url):
    sleep(1)
    header = {"User-Agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header)
        OK_STATUS = 200
        return response.text if response.status_code == OK_STATUS else None
    except ReadTimeout:
        return None


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links_to_news = selector.css("h2.entry-title a::attr(href)").getall()
    return links_to_news


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
