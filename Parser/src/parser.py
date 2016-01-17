#!/usr/bin/env python3

import urllib.request


BASE_URL = 'http://google.com'
BASE_URL1 = 'http://investing.com'
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def main():
    get_html(BASE_URL)
if __name__ == '__main__':
    main()
