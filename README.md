# Python Project: Web Scraping and Data Cleaning

The goal of the project is to create a python script based web scraper that can extract data from wikepedia (keeping in view the directories that are prohibited to be access by 
wikipedia(robot.txt) ) and clean it up.

## Description
I have written a python script that can extract any wikipedia pages given the language of the wikipedia and the name of the article and store the content of those articles in a separate .txt file. The highlight of the project is that it does not scrape just one article input but it starts from one article (or perhaps a set of articles) and following links from those articles to find more articles to download. The article or set of articles are input as titles (not as URLs) and also the name of language is input in whihc Wikipedia contains the target article. In the next step I have cleaned the articles according to the criteria mentioned below and stored a new version of the file in a separate output directory. 
- One sentence per line
- The words in each sentence separated from each other by exactly one space
- Case (upper-case/lower-case) should be removed (normalize to either upper or lower case)

## Important Libraries
- requests
- BeautifulSoup
- Scrapy
- argparse

## References
https://rstudio-pubs-static.s3.amazonaws.com/206871_524d2f90ae0f40c98ceda50d0646f1e2.html#exercise-5-crawling-websites
