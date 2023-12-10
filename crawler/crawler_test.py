#!/usr/bin/python3
import unittest
from crawler import find_articles

class TestFindArticles(unittest.TestCase):
    def test_find_articles(self):
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
        
        # Call the function with test data
        result = find_articles(xpath, html_content)
        
        # Define expected output based on the test HTML content
        expected_output = [
            'https://example.com/page1',
            'https://example.com/page2',
            'https://example.com/page3'
        ]
        
        # Assertion to check if the function output matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
