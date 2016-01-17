#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import string


g = Grab(log_file='out.html')
g.go('http://www.investing.com/commodities/gold-technical')

resp = g.response.body

#print resp
print len(resp)

g.request(log_file='out.htm2')
print len(g.response.body)

search_area = g.xpath_text('//div[@class="techStudiesTabInnerWrap"]')
t = search_area.split();
result = (t[0].split(':'))[1]
i = 1
while (t[i] != 'Moving'):
    result += ' ' + t[i]
    i += 1;

print result
print t

#print string.find(search_area, 'STRONG SELL')
