#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://www.google.com'
BASE_URL1 = 'http://www.investing.com/quotes/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()



def main():
    print(get_html(BASE_URL))


if __name__ == '__main__':
    main()
