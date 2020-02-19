#! python3
# Image downloader - go to imgur.com and search for a category, then download all of the images
'''
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos,
and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
'''

import requests, os, bs4

url = 'https://imgur.com/search?q=' # Starting URL
os.makedirs('imgur', exist_ok=True)

userSearch = 'cat'
url = url + userSearch
#Download the page.
print('Downloading page....')
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

postElem = soup.select('.image-list-link img')
print(postElem)
if postElem == []:
    print('Could not find post image')
else:
    for i in range(len(postElem)):
        imageURL = 'https:' + postElem[i].get('src')

        # Visit the image page
        print('Downloading image %s...' % (imageURL))
        res = requests.get(imageURL)
        res.raise_for_status()
        # Save the image to ./imgur
        imageFile = open(os.path.join('imgur', os.path.basename(imageURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done')
