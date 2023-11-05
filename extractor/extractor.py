import json
from lxml import etree\
import requests

def find_element_by_xpath(html_tree, xpath):
    element = html_tree.xpath(xpath)
    if element:
        return element[0].text
    return None

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        html = response.text
        return html
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    json_data = read_json_file('your_json_file.json')
    domain = json_data['domain']
    html = get_html_from_url(domain)

    for article in json_data['articles_XPath']:
        title = find_element_by_xpath(html, article['title'])
        body = find_element_by_xpath(html, article['body'])
        author = find_element_by_xpath(html, article['author'])
        date = find_element_by_xpath(html, article['Date'])

        if title and body:
            formatted_article = f"Title: {title}\nAuthor: {author}\nDate: {date}\n\n{body}\n"
            print(formatted_article)
