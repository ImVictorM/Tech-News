import requests
from requests.exceptions import ReadTimeout
from time import sleep


def fetch(url):
    sleep(1)
    header = {"User-Agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header)
        OK_STATUS = 200
        return response.text if response.status_code == OK_STATUS else None
    except ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
