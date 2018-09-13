import os
from bs4 import BeautifulSoup as bs
import requests
import urllib3
import certifi
url = 'https://www.pexels.com/search/nature/'

opener = urllib3.PoolManager(
cert_reqs='CERT_REQUIRED',
ca_certs=certifi.where())
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.request('GET', url)


soup = bs(response.data, 'html.parser')

images = soup.findAll('img')

if not os.path.exists('nature'):
    os.makedirs('nature')

os.chdir('nature')

x =16
for i in images:
    try:
        url = i['src']
        source= opener.request('GET', url[:url.index('?')])
        if source.status == 200:
            with open('nature' + str(x) + '.jpg', 'wb') as f:
                f.write(source.data)
                f.close()
                x+=1
    except:
        pass