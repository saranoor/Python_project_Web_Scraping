# -*- coding: utf-8 -*-
"""

"""   
def extract_wikipedia_contents(content):
    from bs4 import BeautifulSoup
    #import requests
    #response = requests.get(url, timeout=5)
    #INPUT_FILE='Stipple-throatedantwren-Wikipedia.html'
    content = BeautifulSoup(content, "html.parser")
    #content.find('div',attrs={"id":""})

    article_txt = content.find('div', attrs={"id": "bodyContent"})
    print(article_txt.find('div',attrs={"class":"noprint"}).text)
    print(article_txt.p.text)
    print(article_txt.find('ul').text)
    
    
if __name__ == "__main__":
# Imports if necessary 
    import argparse
    parser=argparse.ArgumentParser(description='Take the file') 
    parser.add_argument('filename', help='what the argument holds',type=str)
    args=parser.parse_args()
    #print(args.filename)
    with open(args.filename,"r", encoding='utf-8') as f:
        content=f.read() 
    
    article_contents = extract_wikipedia_contents(content)   
    
