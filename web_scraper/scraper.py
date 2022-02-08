from calendar import c
from email import parser
from unittest import result
import requests
import time
import urllib.request
from bs4 import BeautifulSoup

# set url to scrape
url = 'https://en.wikipedia.org/wiki/Triple_J#1970s:_Launch_and_early_years'


def get_citations_needed_count(url):
    citation_needed_count = 0
    
    # connect to url and get response
    page = requests.get(url)

    # set beautifulsoup object
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup)
    # find citation needed string in the link.
    results = soup.findAll("span", string="citation needed")
    # loop through and increment the citation needed count.
    for count in results:
        citation_needed_count= citation_needed_count + 1
       
    
    return f'Total citations needed:  {citation_needed_count}'

 


def get_citations_needed_report(url):
    relevant_passage = []
    page = requests.get(url)

    # set beautifulsoup object
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup)
    # find citation needed string in the link.
    results = soup.find_all("span")
    need_citation = "citation needed"

    for passage in results:
        if passage.string == need_citation:
            find_prev = passage.find_parents("p")
            find_prev = print(str(find_prev)[4:100], "\n")
            relevant_passage.append(find_prev)

    return relevant_passage




print(get_citations_needed_report(url))
  
print(get_citations_needed_count(url))
