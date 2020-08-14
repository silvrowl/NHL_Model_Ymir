#!/usr/bin/env python
# coding: utf-8

# Script containing parsers for text and dates for different sites

import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import dateparser

def base_parser(text, base_site):

    site_list = []
    
    if base_site in site_list:
        #Use specific parser
        print('Using Specific Parser')
    
    else:
    
        # web elements to ignore
        output = ''
        blacklist = [
            '[document]',
             'a',
             'aside',
             'article'
             'b',
             'body',
             'div',
             'fieldset',
             'figure',
             'footer',
             'form',
             'h1',
             'h2',
             'h6',
             'head',
             'header',
             'html',
             'input',
             'li',
             'link',
             'meta',
             'noscript',
             'script',
             'section',
             'span',
             'strong',
             'style',
             'time',
             'title',
             'ul',
             'button',
             'svg']

        test = ''
        
        for t in text:
            if t.parent.name not in blacklist:
                
                # Append text across all elements
                test += t.parent.name
                
                output += '{} '.format(t)

        final = output.replace('\n','')
    
    return final


def time_parser(soup, base_site):
    
    #Sites
    site_list = ['www.sportsnet.ca','www.nhl.com','www.tsn.ca','thehockeywriters.com','globalnews.ca','torontosun.com']
    
    if base_site in site_list:
            
        if base_site == 'torontosun.com':
            
            spans = soup.find_all('span', {'class' : 'published-date__since'})
            
            print('hello')
            
            lines = [span.get_text() for span in spans]
            
            final = dateparser.parse(lines[0])
        
        
        if base_site == 'globalnews.ca':
            
            spans = soup.find_all('div', {'class' : 'c-byline__date c-byline__date--pubDate toggle-switch'})
            
            lines = [span.get_text() for span in spans]
            
            date = lines[0]
            
            #print(date[8:])
            
            final =  dateparser.parse(date[8:])
        
        if base_site == 'www.sportsnet.ca':
            
            spans = soup.find_all('span', {'class' : 'article-publish-date'}) 
            lines = [span.get_text() for span in spans]
            
            if len(lines)>0:
                final = dateparser.parse(lines[0])
            
            else:
                spans = soup.find_all('div', {'class' : 'tands-date'})
                lines = [span.get_text() for span in spans]

            if len(lines)>0:
                final = dateparser.parse(lines[0])
                
            else: 
                final = 'NaN'
            
        if base_site == 'thehockeywriters.com':
            
            spans = soup.find_all('span', {'itemprop' : 'dateCreated'})
            
            lines = [span.get_text() for span in spans]
            
            final = dateparser.parse(lines[0])
            
            
        if base_site == 'www.nhl.com':
            
            spans = soup.find_all('span', {'class' : 'article-item__date'})
            
            #print(spans)
            
            lines = [span.attrs['data-date'] for span in spans]
            
            final = dateparser.parse(lines[0])
            
        if base_site == 'www.tsn.ca':
            
            spans = soup.find_all('div', {'class' : 'date'})
            
            #print('test')
            
            lines = [span.get_text() for span in spans]
            
            final = dateparser.parse(lines[0].replace('\n','').strip())
    
    else:
        
        # default parser
        final = 'Nan'    
        for i in soup.findAll('time'):
            if i.has_attr('datetime'):
                final = dateparser.parse(i['datetime'])
    
    
    return final
