"""Etracting one article (or perhaps a set of articles) and following links from those 
articles to find more articles to download

Args:text file containing list of titles 
Return:none

"""

import argparse
from requests import get
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import wikipedia_F2 as wp
import pandas as pd
import csv
import check_url as ch

def extract_wikipedia_articles(titles_list):
    with open(titles_list, newline='',encoding='cp1252', errors='ignore') as csvfile:
        fieldnames=['Title','Language']
        reader = csv.DictReader(csvfile, fieldnames = fieldnames, dialect='excel')
        #reader = csv.DictReader(csvfile)
        next(reader)
        cnt=0
        url_fetched=[]
        for row in reader:
            cnt+=1
            print(row['Title'], row['Language'])
            url='https://'+row['Language']+'.wikipedia.org/wiki'+'/'+row['Title']
            url_fetched.append(url)
            while(cnt<50):
                #print(url)
                response=get(url)
                #link_list=[]
                if response.status_code==200 :
                            link_list=[]
                            page_html = BeautifulSoup(response.text, 'html.parser')
                            print('I am in', cnt)
                            print('\n')
                            article_content=wp.extract_wikipedia_contents(page_html)
                            #url_fetched.append(url)
                            with open('article'+'['+str(cnt)+'].txt','w', errors='ignore') as f:
                                f.write(article_content)
                            
                            for link in page_html.find_all('a', title=True):
                                #if  (link['href'].find('https://')>=0):
                                    #print(cnt,'link not allowed:', link)
                                    
                                if (link['href'].find('https://')==-1):
                                    link_list.append(link['href'])
                            c_l_l=0
                            while(c_l_l<len(link_list)):
                                #link_=link_list[c_l_l]
                                #link_=link_[link_.find('/wiki'):]
                                found=0
                                url='https://'+row['Language']+'.wikipedia.org'+link_list[c_l_l]
                                for url_fetch in url_fetched:
                                    url_fetch=url_fetch.split("#")[0]
                                    if (url.find(url_fetch)>=0):
                                        url='https://'+row['Language']+'.wikipedia.org'+link_list[c_l_l]
                                        print('Article already in fetched list \n')
                                        c_l_l+=1
                                        found=1
                                        break
                                
                                if found==0:
                                    check=ch.check_url(link_list[c_l_l])
                                    if check==-1:
                                        
                                        print('Link to be fetched', link_list[c_l_l])
                                        print('Complete link', url)
                                        print('Lets see if ended')
                                        print('\n')
                                        url_fetched.append(link_list[c_l_l])
                                        c_l_l+=1
                                        break
                                    else: 
                                        c_l_l+=1
                            cnt+=1
                else:
                     print('Error in fetching this url:',url)
                     while(c_l_l<len(link_list)):
                                #link_=link_list[c_l_l]
                                #link_=link_[link_.find('/wiki'):]
                                found=0
                                url='https://'+row['Language']+'.wikipedia.org'+link_list[c_l_l]
                                for url_fetch in url_fetched:
                                    url_fetch=url_fetch.split("#")[0]
                                    if (url.find(url_fetch)>=0):
                                        url='https://'+row['Language']+'.wikipedia.org'+link_list[c_l_l]
                                        c_l_l+=1
                                        found=1
                                        print('Already fetched',link_list[c_l_l])
                                        print('\n')
                                        break
                                
                                if found==0:
                                    check=ch.check_url(link_list[c_l_l])
                                    if check==-1:
                                        
                                        print('Link to be fetched', link_list[c_l_l])
                                        print('Complete link', url)
                                        print('Lets see if ended')
                                        url_fetched.append(link_list[c_l_l])
                                        c_l_l+=1
                                        break
                                    else: 
                                        c_l_l+=1
                     
            print(url_fetched)
            break


if __name__ == "__main__":
    LANG_FILE='lang_list.csv'
    parser=argparse.ArgumentParser(description='Take the file') 
    parser.add_argument('filename', help='what the argument holds',type=str)
    args=parser.parse_args()
    print(args.filename)
    extract_wikipedia_articles(args.filename) 
    print('done')
    






















   