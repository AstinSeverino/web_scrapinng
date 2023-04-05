#import librerys 
import requests
import lxml.html as html
import os 

#xpath links 
URL_PAGE = 'https://news.ycombinator.com'
XPATH_LINK = '//span[@class="titleline"]/a/@href'
XPATH_TEXT = '//span[@class="titleline"]/a/text()'
XPATH_SCORE = '//span[@class="subline"]/span[@class="score"]/text()'
XPATH_DATE = '//span[@class="subline"]/span[@class="age"]/@title'

def parse_home():
    try:
        response = requests.get(URL_PAGE)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            notice = parsed.xpath(XPATH_TEXT)
            print(notice)
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(f"Has ocurre a error")

def run():
    parse_home()

if __name__ == '__main__':
    run()