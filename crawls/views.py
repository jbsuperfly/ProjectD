from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
# from django.template import loader
from bs4 import BeautifulSoup
from datetime import datetime
import json as simplejson
import urlparse
import urllib2 #allows for urlopen function
import requests
import pprint #prints nicely
import random #allows for random time interval
import time #allows for time interval
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Create your views here.
def index(request):
    return render(request, 'crawls/index.html')
def home(request):
    return render(request, 'crawls/index.html')
def search_url(request):
    errors = []
    if not request.POST['url']:
        errors.append('You need a URL for this to work')
        return render(request, 'crawls/index.html', {'errors': errors})
    else:
        url = request.POST['url'] #url you want to scrape/crawl through
        try:
            urllib2.urlopen(url)
        except:
            print 'ERROR: '+url+' does not exist'
        else:
            source_code = requests.get(url) # gets the code for the page. allowing the crawler to crawl through
            plain_text = source_code.text # turns code into text
            soup = BeautifulSoup(plain_text) #generates the text
            soup = str(soup)
            #converts object to a string
            # print (soup)
            tags = []
            idx = 0
            i = 0
            line = ""
            while i < len(soup):
                if soup[i] == '\n':
                    line+=soup[i]
                    tags.insert(idx, line)
                    line = ""
                    idx+=1
                    i+=1
                elif soup[i] == ' ':
                    i+=1
                else:
                    line+=soup[i]
                    i+=1
            # print (soup)
            return render(request, 'crawls/success.html', {'tags': tags, 'url': url
            })
def search_deeper(request):
    errors = []
    if not request.POST['search']:
        errors.append('You need to give me something to search for')
        return HttpResponseRedirect(reverse('crawls:index', errors=errors))
    else:
        url = request.POST['url'] #url you want to scrape/crawl through
        search = request.POST['search']#what you search for
        source_code = requests.get(url) # gets the code for the page. allowing the crawler to crawl through
        plain_text = source_code.text # turns code into text
        soup = BeautifulSoup(plain_text) #generates the text
        soup = str(soup)
        tags = []
        idx = 0
        i = 0
        line = ""
        while i < len(soup):
            if soup[i] == '\n':
                line+=soup[i]
                if line.find(search) != -1:
                    tags.insert(idx, line)
                    line = ""
                    idx+=1
                    i+=1
                else:
                    line = ""
                    i+=1
            elif soup[i] == ' ':
                i+=1
            else:
                line+=soup[i]
                i+=1
        if len(tags) < 1:
            tags.insert(idx, 'Your Search Has Returned Nothing')
        # print (soup)
        return render(request, 'crawls/success.html', {'tags': tags, 'url': url
        })
def search_deepest(request):
    url = request.POST['url'] #url you want to scrape/crawl through
    source_code = requests.get(url) # gets the code for the page. allowing the crawler to crawl through
    plain_text = source_code.text # turns code into text
    soup = BeautifulSoup(plain_text) #generates the text
    soup = str(soup)
    soup = simplejson.dumps(soup)
    return render(request, 'crawls/matrix.html', {'soup': soup, 'url': url
    })
