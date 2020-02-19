#! python3
# Image downloader - go to imgur.com and search for a category, then download all of the images


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

postElem = soup.select('.post .image-list-link')
if postElem == []:
    print('Could not find post image')
else:
    imageURL = 'https://imgur.com' + postElem[0].get('href')

    # Visit the image page
    print('Visiting image %s...' % (imageURL))
    imageRes = requests.get(imageURL)
    imageRes.raise_for_status()
    soup = bs4.BeautifulSoup(imageRes.text, 'html.parser')
    imageElem = soup.findAll('img')
    print(imageElem)
    for image_tag in imageElem:
        print(image_tag.get('src'))
    # imageURL = 'https:' + imageElem[0].get('src')



# Save the image to ./imgur
# imageFile = open(os.path.join('imgur', os.path.basename(imageURL)), 'wb')
#for chunk in res.iter_content(100000):
#    imageFile.write(chunk)
#imageFile.close()


print('Done')
