import json
from lxml import etree, html
import requests

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def find_element_by_xpath(html_tree, xpath):
    element = html_tree.xpath(xpath)
    if element:
        element_text = element[0].text.strip() if element[0].text else element[0].text_content().strip()
        return element_text
    print(f" Couldn't find {xpath}")
    return None


def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        html = response.text
        #print(html)
        return html
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    json_data = read_json_file('test.json')
    domain = json_data['domain']
    html_source = get_html_from_url(domain)

    html_etree = html.fromstring(html_source)
    title = find_element_by_xpath(html_etree, json_data['title'])
    body = find_element_by_xpath(html_etree, json_data['body'])
    author = find_element_by_xpath(html_etree, json_data['author'])
    date = find_element_by_xpath(html_etree, json_data['date'])

    if title and body:
        
        formatted_article = f"Domain: {domain}\nTitle: {title}\nAuthor: {author}\nDate: {date}\n\n{body}\n"
        print(formatted_article)
    