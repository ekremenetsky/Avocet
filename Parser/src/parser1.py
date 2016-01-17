#!/usr/bin/env python3 
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from urllib import urlopen

html_doc = urlopen('http://python-3.ru').read()
soup = BeautifulSoup(html_doc)

