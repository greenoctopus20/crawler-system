#!/usr/bin/python3

from lxml import html
import requests
import traceback
import json
from rabbitmq import consume_message, produce_message
from pprint import pprint 
import pickle
from model import Crawled, Session


def find_articles(article_xpath: str, html_content: str, domain : str):
    
    articles_links = []
    page_html = html.fromstring(html_content)
    links = page_html.xpath(article_xpath)
    for link in links: 
        if link is not None:
            #link = link.get("href")
            if "HtmlElement" in str(type(link)):
                link = link.get("href")
            #print(type(link))
            if "ElementUnicodeResult" in str(type(link)):
                link = link.__str__()                
            if domain not in link:
                link = domain + link
                articles_links.append(link)
            else:
                articles_links.append(link)
    return articles_links


def get_articles(links):
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            print("passed")
            # Save Extracted HTML
            #save_document(response.text)
            


def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        html = response.text
        return html
    except requests.exceptions.RequestException as e:
        #print(f"Error: {e}")
        return None

def save_html(html, body):
    session = Session()
    new_record = Crawled(
                    site_id=1,
                    url='https://example.com',
                    date='2023-12-14',
                    code_status=200,
                    html=str(html)
                )
    session.add(new_record)
    session.commit()
    print("New record created:", new_record)

def process(ch, method, properties, body):
    try:
        print("Received new message")
        print("********")
        data = pickle.loads(body)
        print(data)
        print("********")
        html = get_html_from_url(data['domain_url'])
        save_html(html, body)
        article_links = find_articles(data['article_xpath'], html , data['domain_url'])
        data['links'] = article_links[:3]
        message = json.dumps(data)
        print(data)
        produce_message(message)
        print("Sent message to extractor")
    except Exception as E:
        print(E)
        print(traceback.format_exc())

        
if __name__ == '__main__':
    consume_message(callBack=process)
