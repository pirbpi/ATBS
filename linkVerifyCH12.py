#! python3
# Verify all links on a given webpage
'''
Write a program that, given the URL of a web page, will attempt to download every linked page on the page.
The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
'''
import requests, bs4

testingURL = 'https://www.michigan.gov/minewswire/0,4629,7-136-3452---,00.html'
res = requests.get(testingURL)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.indexTitle a')

for i in range(len(linkElems)):
    print(linkElems[i].get('href'))
    reachableURL = linkElems[i].get('href')
    if reachableURL[0] == '/':
        reachableURL = requests.get('https://www.michigan.gov' + linkElems[i].get('href'))
    else:
        reachableURL = requests.get(linkElems[i].get('href'))
    try:
        reachableURL.raise_for_status()
    except:
        print('Unable to reach %s' % (linkElems[i]))
        continue
