'''
RUN THE SCRIPT, INPUT THE SLIDESHARE URL AND HIT ENTER!!

YOU WILL SEE THE LINKS FOR ALL THE IMAGES OF THE SLIDES, DOWNLOAD THEM AS YOU GO!!

JUST AND AN EMPTY SPACE AFTER YOU INPUT THE URL,,,
'''

import requests, bs4, urllib


def get_url():
    url = input('URL: ')
    print()
    return url


def get_html(url):
    data = requests.get(url)
    return data


def get_all_images(url):
    number = 1
    html_data = get_html(url)
    soup = bs4.BeautifulSoup(html_data.text, 'html.parser')
    soop = soup.find_all(
        class_="slide_image")  # find class named slide_image, beacause that is the class our images are in
    for i in soop:
        img_src = i['data-full']
        filename = str(number)
        img_file = open(filename + ".jpeg", 'wb')
        img_file.write(urllib.request.urlopen(img_src).read())
        img_file.close()

        number += 1
    return img_src


print(get_all_images(get_url()))
