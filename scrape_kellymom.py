from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
from urllib import urlencode
import pandas as pd

browser = webdriver.Firefox()


def search_kellymom(query, browser):
    '''
    basic search function to get page_source information
    '''
    base_url = "http://kellymom.com/?{}"
    search_url = base_url.format(
        urlencode([('s', query)])
        )
    browser.get(search_url)
    return browser.page_source

def get_article_tags(query, browser):
    """Return the article tag associated with each article found in search.

    Arguments
    ---------
    query

    Returns
    -------
    article_tag : bs4.element.Tag
    """
    html = search_kellymom(query, browser)
    soup = BeautifulSoup(html, 'html.parser')
    article_tags = soup.select('article.post')
    return article_tags

def get_article_title(article_tag):
    """Return the title of an article selected from kellymom.com site.

    If no title element is found, return None.

    Arguments
    ---------
    article_tag : bs4.element.Tag
        article.post (from kellymom.com)

    Returns
    -------
    article_titles : list
    """

    title_tag = article_tag.select('h2.entry-title')
    title = title_tag[0].text
    if type(title) == unicode:
        title = title.encode('utf8')

    return title

def get_article_link(article_tag):
    """Return the link of an article from kellymom.com site.

    If no link element is found, return None.

    Arguments
    ---------
    article_tag : bs4.element.Tag
        article.post (from kellymom.com)

    Returns
    -------
    article_links : list
    """
    links = []

    http_tag = article_tag.select('h2.entry-title')
    http = str(http_tag[0].a)
    http = http.split()
    link = http[1]
    link = link[6:-1]
    return link

def get_content(link, browser, delay=2):
    '''
    Return the content of a selected link from kellymom.com site.


    Arguments
    ---------
    link : string object

    Returns
    -------
    article_content : list
    '''
    browser.get(link)
    time.sleep(delay)  # Wait a few seconds before getting the HTML source
    source = browser.page_source
    soup = BeautifulSoup(source, 'html.parser')
    content_list = soup.select('div.entry-content')
    content = content_list[0].text
    return content.encode('ascii', 'ignore').strip().replace('\n', '').replace('                   ', ' ')

def build_corpus(queries, browser):
    '''
    Takes a search term and returns the title, link and content for all articles with that term

    Arguments
    ---------
    query : list of strings

    Returns
    -------
    corpus : list of rows, with each row containing the title, url and content of each article

    '''
    article_tags = []
    for query in queries:
        article_tag_prelim = get_article_tags(query, browser)
        for article_tag in article_tag_prelim:
            if article_tag not in article_tags:
                article_tags.append(article_tag)

    return [(get_article_title(t), get_article_link(t), get_content(get_article_link(t), browser)) for t in article_tags]

if __name__ == '__main__':
    search_terms = ['nutrition', 'food', 'eat', 'meal', 'formula', 'nutrients', 'vitamins', 'supplements', 'diet', 'wellness',]
    corpus = build_corpus(search_terms, browser)
    ! touch kelly_mom.csv
    with open('kelly_mom.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(corpus)
