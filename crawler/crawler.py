#!/usr/bin/python3

from lxml import html
import requests
import json

def find_articles(article_xpath: str, html_content: str):
    articles_links = []
    page_html = html.fromstring(html_content)
    links = page_html.xpath(article_xpath)
    for link in links: articles_links.append(link)
    return articles_links


def get_articles(links):
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            # Save Extracted HTML
            save_document(response.text)
        else:
            # Save failed links
            save_failed_link(link)
            
def save_document(html):
    print("Saved")

def save_failed_link(link):
    print("Failed link saved")

