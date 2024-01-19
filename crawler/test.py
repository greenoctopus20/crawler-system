#!/usr/bin/python3
import unittest
import logging
from crawler import find_articles , get_html_from_url

class TestFindArticles(unittest.TestCase):
    def test_Find_articles_in_html(self):
        # Test case
        html_content = '''
        <html>
            <body>
                <a href="https://example.com/page1">Link 1</a>
                <a href="https://example.com/page2">Link 2</a>
                <a href="https://example.com/page3">Link 3</a>
            </body>
        </html>
        '''
        xpath = '//a/@href'
        result = find_articles(xpath, html_content , "https://example.com")
        expected_output = [
            'https://example.com/page1',
            'https://example.com/page2',
            'https://example.com/page3'
        ]
        self.assertEqual(result, expected_output)
        
    def test_Get_html_from_domain(self):
        # this is new site i created 
        url = 'http://206.189.240.137//' 
        result = get_html_from_url(url)
        self.assertEqual(len(result), 2183)
        
    def test_Get_html_from_invalid_site(self):
    
        url = 'www.this_is_not_a_site.co'
        result = get_html_from_url(url)
        self.assertEqual(result, None)
        

if __name__ == '__main__':
    unittest.main()
