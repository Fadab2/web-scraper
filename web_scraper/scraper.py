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

 

# anchors = results('a')
# #print(anchors)
# links = [anchor['href'] for anchor in anchors]
# citation_link = links[0]
# # for link in links:
# #     print(link)
# #print(citation_link)


# citation_url = 'https://en.wikipedia.org/wiki/Triple_J#1970s:_Launch_and_early_years' + citation_link

# #print(citation_url)

# citation_content = requests.get(citation_url)

# content_soup = BeautifulSoup(citation_content.content, 'html.parser')
# #print(citation_content.content)

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
