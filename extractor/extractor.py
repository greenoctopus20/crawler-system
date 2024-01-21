import json
from lxml import etree, html
import requests
from rabbitmq import consume_message , produce_message
from pprint import pprint
from models import Session, articles
import time

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def find_element_by_xpath(html_tree, xpath):
    try:
        elements = html_tree.xpath(xpath)
        if elements:
            element_text = elements[0].text_content().strip() if elements[0].text else elements[0].strip()
            return element_text
    except Exception as E:
        print(f"SOMETHING WRONG {E}")
    #print(f" Couldn't find {xpath}")
    return None



def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        html = response.text
        print(len(html))
        return html
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def save_article(id, title, article_body, url, author=None, date=None ):
        session = Session()
        new_record = articles(
            site_id=id,
            url=url,
            title=title,
            author=author,
            body=article_body,
            date=date
        )
        session.add(new_record)
        session.commit()
        print(f"New Article Saved with tile {title}")

def process(ch, method, properties, body):
    print("Received A message")
    print("***********")
    payload = json.loads(body)
    print(payload)
    print("***********")
    
    #try:
    for link in payload['links']:
        print(link)
        html_source = get_html_from_url(link)
        if html_source:
            html_etree = html.fromstring(html_source)
            title = find_element_by_xpath(html_etree, payload['title_xpath'])
            article_body = find_element_by_xpath(html_etree, payload['body_xpath'])
            author = find_element_by_xpath(html_etree, payload['author_xpath']) 
            date = find_element_by_xpath(html_etree, payload['date_xpath'])                
            if title and article_body:
                save_article(payload['id'],title, article_body, link, author, date)
                formatted_article = f"Link: {link}\nTitle: {title}\nAuthor: {author}\nDate: {date}\n\n{article_body}\n"
                print(formatted_article)
    #except Exception as e:
    #    print(e)

if __name__ == "__main__":
    #json_data = read_json_file('test.json')
    #produce_message(json_data)
    consume_message(callBack=process)
    
