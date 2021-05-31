#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An RFC 5321 smtp proxy with optional RFC 1870 and RFC 6531 extensions.
Usage: %(program)s [options] [localhost:localport [remotehost:remoteport]]
Options:
    --nosetuid
    -n
        This program generally tries to setuid `nobody', unless this flag is
        set.  The setuid call will fail if this program is not run as root (in
        which case, use this flag).
    --version
    -V
        Print the version number and exit.
    --class classname
    -c classname
        Use `classname' as the concrete SMTP proxy class.  Uses `PureProxy' by
        default.
    --size limit
    -s limit
        Restrict the total size of the incoming message to "limit" number of
        bytes via the RFC 1870 SIZE extension.  Defaults to 33554432 bytes.
    --smtputf8
    -u
        Enable the SMTPUTF8 exension and behave as an RFC 6531 smtp proxy.
    --debug
    -d
        Turn on debugging prints.
    --help
    -h
        Print this message and exit.
Version: %(__version__)s
If localhost is not given then `localhost' is used, and if localport is not
given then 8025 is used.  If remotehost is not given then `localhost' is used,
and if remoteport is not given, then 25 is used.
"""
# TODO: add command line arguments to manipulate the data
# TODO: update the project description
# TODO: clean up the code
import argparse
from utils.utils import sqlite_connect
import requests
from bs4 import BeautifulSoup
import pandas as pd
from bs4 import SoupStrainer
from datetime import datetime

TODAY = datetime.today().strftime('%Y-%m-%d')


def extract(title: str, location: str) -> BeautifulSoup:
    """
    Returns a BeautifulSoup object from indeed.com.
    :param title: Desired Job title
    :param location: Desired location
    :return: content used for parsing
     """
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
    return soup


def transform(content: BeautifulSoup) -> pd.DataFrame:
    """ Parses the page contents """
    joblist = []
    divs = content.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        # try:
        #     salary = item.find('span', class_='salaryText').text.strip()
        # except:
        #     salary = ''
        # summary = item.find('div', class_='summary').text.strip().replace('\n', '')
        url = f"https://www.indeed.com{item.h2.a.get('href')}"

        job = {
            'title': title,
            'company': company,
            # 'salary': salary,
            # 'summary': summary,
            'date_applied': TODAY,
            'url': url
        }

        joblist.append(job)

    return pd.DataFrame(joblist)


soup = extract('Data Analyst', 'Toronto')

df = transform(soup)
print(df.to_string())
# df.to_csv('jobs.csv')
conn = sqlite_connect()
#
# print('Connected')
#
# while True:
#     break
#
# conn.close()

# parser = argparse.ArgumentParser()
# parser.add_argument()
