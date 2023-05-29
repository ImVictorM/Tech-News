import requests
from requests.exceptions import ReadTimeout
from time import sleep
from parsel import Selector
from tech_news.database import create_news
import re


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


def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()

    writen_time = selector.css("li.meta-reading-time:last-child::text").get()
    only_numbers_reading_time = int(re.findall(r"\d+", writen_time)[0])

    first_p = selector.css("div.entry-content p").get()
    summary = "".join(Selector(text=first_p).css("*::text").getall())

    category = selector.css("a.category-style span.label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": only_numbers_reading_time,
        "summary": summary.strip(),
        "category": category,
    }


def extract_links_to_scrape(amount):
    amount = int(amount)
    home_endpoint = "https://blog.betrybe.com/"
    home_html = fetch(home_endpoint)
    main_page_content = scrape_updates(home_html)

    links_to_scrape = []
    links_to_scrape.extend(main_page_content[:amount])

    next_page_link = scrape_next_page_link(home_html)

    while len(links_to_scrape) < amount:
        next_page_content = fetch(next_page_link)
        links_to_scrape.extend(scrape_updates(next_page_content))
        next_page_link = scrape_next_page_link(next_page_content)

    return links_to_scrape[:amount]


def scrape_multiple_links(links_to_scrape):
    scraped_content = []

    for link in links_to_scrape:
        html = fetch(link)
        scraped_content.append(scrape_news(html))

    return scraped_content


def get_tech_news(amount):
    links_to_scrape = extract_links_to_scrape(amount)
    scraped_content = scrape_multiple_links(links_to_scrape)

    create_news(scraped_content)
    return scraped_content
