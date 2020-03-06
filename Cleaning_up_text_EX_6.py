# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:22:02 2019

@author: skm
"""

import ast
import sys
import argparse
import os
import re
"""
Clean up text of article; One sentence per line; All lower case; words in each sentence 
separated by exactly one space. 

Args: 
    a name of directory and a list of articles
Return:  
    None

"""
def cleaning_up_text(dir_name, list_arc):
    cnt=1
    for l_arc in list_arc:
        with open(l_arc, 'r', errors='ignore') as arc:
            content=arc.read()
            
            if cnt==2:
                print(content)
                print('lets print')
            #content
            content=content.replace(',\n', ', ')
            content=content.replace('. ', '.\n')
            content=content.replace('...\n', '... ')
            content=re.sub(r'\n+', '\n',content)
            content=re.sub( r'(\.\[[^][]*\])\s*', r'\1\n', content)
            #print(content)
            with open( os.path.join(dir_name, str(l_arc) ), 'w', errors='ignore') as marc:
               marc.write(content)
            #for i in content:
            #    print(i)
            #content
            cnt=cnt+1
            
        
    return

 
 
if __name__ == "__main__":
    LANG_FILE='lang_list.csv'
    parser=argparse.ArgumentParser(description='Take the file') 
    parser.add_argument('--Dir_name', help='what the argument holds',type=str)
    #parser.add_argument('list_arc', help='what the argument holds',type=str)
    parser.add_argument('--details', nargs='*', type=list)
    args=parser.parse_args()
    
    print(args.Dir_name)
    #print(args.details)
    print(sys.argv[4])
    '''s2=sys.argv[2]
    s2=s2.strip('][')
    s2=s2.split(',')
    print(s2)
    print(type(s2))
    for i in s2:
        print(i)'''

    str_arc=sys.argv[4]
    list_arc = ast.literal_eval(str_arc)
    print('lets call')
    cleaning_up_text(args.Dir_name, list_arc)
    
    #print(type(list_arc))
    #print(list_arc)
    #for i in list_arc:
    #    print(i)



'''
list_arc=[]
import os
for file in os.listdir("E:\python_libraries\python\Project Wikipedia web crawling"):
    if file.endswith(".txt") and file.startswith("a"):
        file=file.rstrip("\n\r")
        list_arc.append(file)'''
