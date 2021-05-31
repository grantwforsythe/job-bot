import argparse
import requests
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

def extract(title: str, location: str) -> BeautifulSoup:
    """
    Returns a BeautifulSoup object from indeed.com.
    :param title: Desired Job title
    :param location: Desired location
    :return: content used for parsing
     """
    soup = None

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/90.0.4430.212 Safari/537.36'}

    content = SoupStrainer('table', {'id': 'pageContent'})

    r = requests.get('https://ca.indeed.com/jobs',
                     params={'q': title, 'l': location},
                     headers=headers,
                     timeout=3
                     )
    if r.ok:
        soup = BeautifulSoup(r.content,
                             features='html.parser',
                             parse_only=content
                             )
    else:
        raise ValueError("Invalid URL, please entry valid arguments.")
    return soup


def transform(content: BeautifulSoup) -> pd.DataFrame:
    """ Parses the page contents """
    joblist = []
    divs = content.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        url = f"https://www.indeed.com{item.h2.a.get('href')}"

        job = {
            'title': title,
            'company': company,
            'url': url
        }

        joblist.append(job)

    return pd.DataFrame(joblist)