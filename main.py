##import librerys 
import requests 
import lxml.html as html
import os 
import datetime
import json

#xpath links 
URL_PAGE = 'https://news.ycombinator.com'
XPATH_LINK = '//span[@class="titleline"]/a/@href'
XPATH_TEXT = '//span[@class="titleline"]/a/text()'
XPATH_SCORE = '//span[@class="subline"]/span[@class="score"]/text()'
XPATH_DATE = '//span[@class="subline"]/span[@class="age"]/@title'

def parse_home():
    try:
        response = requests.get(URL_PAGE,timeout= 5) #time of the request 
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            # scrapinng
            text= parsed.xpath(XPATH_TEXT)
            score= parsed.xpath(XPATH_SCORE)
            date= parsed.xpath(XPATH_DATE)
            link= parsed.xpath(XPATH_LINK)            
            
            # saveing in a dict

            today = datetime.date.today().strftime('%d,%m,%Y') # data saver 

            if not os.path.isdir(today):
                os.mkdir(today)

            with open(f'{today}/{text[0]}.txt', 'a', encoding ='utf-8') as f:
                data = {'title': text, 'score': score, 'date': date, 'link': link}
                f.write(json.dumps(data)) #json.dumps help to save    
                
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as e:
        print(f"Has ocurre a error: {e}")   

  

def run():
    parse_home()

if __name__ == '__main__':
    run()