# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:53:23 2019

@author: skm
"""

import argparse
from requests import get
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import wikipedia as wp
"""filter url using robot.txt
Args:text file containing list of url 
Return:none

"""

def extract_wikipedia_urls(url_file):

    #print('i am here')
    status=load_robots_txt()
    #print(status)
    if status=='All allowed':
        print('All url are allowed')
        with open(url_file,"r", encoding='utf-8') as f:
            for url_part in f:
                url='https://en.wikipedia.org'+url_part.rstrip("\n\r")
                response=get(url)
                page_html = BeautifulSoup(response.text, 'html.parser')
                article_content= wp.extract_wikipedia_contents(page_html)
                print('\n')

    elif status=='some allowed':
        check=-1
        #print('Some url are allowed to scrap')
        infile = open('names.csv', 'r')
        lines=infile.readlines()
        with open(url_file, 'r',encoding='utf-8') as fp:
            for url_part in fp:
                check=-1
                #print(url_part, 'yes')
                for line in lines:
                    #print('url_part',url_part)
                    #print('line',line)
                    line=line.rstrip("\n\r")
                    if (url_part.find(line)==0):
                        
                        url='https://en.wikipedia.org'+url_part.rstrip("\n\r")
                        print('can not access this url:',url)
                        print('\n')
                        check=0
                        break
                #print('check')
                if (check==-1) & (url_part!='\n'):
                    print('can access ')
                    url='https://en.wikipedia.org'+url_part.rstrip("\n\r")
                    print(url,':this is the url we are trying to scrap on your demand')
                    response=get(url)
                    print(response)
                    if response.status_code==200 :
                        page_html = BeautifulSoup(response.text, 'html.parser')
                        article_content= wp.extract_wikipedia_contents(page_html)
                        print(article_content)
                    else:
                        print('No response from the url')
                    print('\n')
           
    elif status=='not allowed':
        print('can not extract any url as not allowed')         

'''def extract_wikipedia_contents(page_content):
    content=page_content.findAll('p')
    return content
    return content[0].text.strip().split('\n')'''
            
""" Create a data structure containing the sites disallow.
If all the sites are allowed to data it returns 'allowed';
If all the sites are excluded to data it returns 'no allowed';
If some urls are excluced return 'some allowed'; create a data structure 
Args: none
Return: status"""   

import csv
def load_robots_txt():
    infile = open('robots.txt',"r",encoding="utf-8")
    numline=0
    line=infile.readlines()
    flag='not_found'
    with open('names.csv', 'w',encoding="utf-8",newline='') as csvfile:
                        fieldnames = ['first_name']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
    while numline<len(line):
        
        line_strip = line[numline].strip()
        if line_strip=='User-agent: *': 
            flag='found'
            numline+=1
            line_strip = line[numline].strip()
            part=line_strip.split()
            while (numline<len(line)):
                if not line[numline].strip():
                   
                    numline+=1
                elif (part[0]=='User-agent:'):
                    break
                elif part[0]=='Disallow:':
                    if len(part)==1:
                        return 'All allowed'
                        break
                    elif part[1]=='/':
                        return 'not allowed'
                        break
                    else:
                        #print(numline, 'part[0]',part[0],'part[1]',part[1])
                        with open('names.csv','a',errors="ignore",newline="") as f:
                            writer = csv.DictWriter(f,fieldnames)
                            writer.writerow({'first_name': part[1]})

                    numline+=1
                else:
                    
                    numline+=1
                if numline<len(line):
                    if not line[numline].strip():
                        print('lets see what happen')
                    else:
                        line_strip = line[numline].strip()
                        
                        part=line_strip.split()

        else:
            numline+=1
    #return 'all allowed' if did not find user-agent:*
    if flag=='not_found':
        return 'all allowed'    
    else:
        return 'some allowed'


'''if __name__ == "__main__":

    parser=argparse.ArgumentParser(description='Take the file') 
    parser.add_argument('filename', help='what the argument holds',type=str)
    args=parser.parse_args()
    print(args.filename)
    extract_wikipedia_urls(args.filename) 
    print('done')

 '''   