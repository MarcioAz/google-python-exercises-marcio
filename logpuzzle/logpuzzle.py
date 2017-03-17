#!/usr/bin/python
# -*-coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def myFunction(link_part):

    return link_part.split('-')[2].split('.')[0]

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file, extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into increasing order."""
    # +++your code here+++
    f = open(filename,'r')
    page = f.read()
    f.close()

    raw_urls = re.findall('GET \S*?(/images/puzzle\S*?) HTTP', page)  # \S matches any non-space character

    raw_urls = list(set(raw_urls))

    raw_urls = sorted(raw_urls, key=myFunction)

    urls = []

    for link in raw_urls:
        urls.append('https://developers.google.com/edu/python' + link)

    # https://developers.google.com/edu/python/images/puzzle/a-baaa.jpg

    #print(len(urls)) # Obs: len(urls) com seleção à procura de 'puzzle': 20; com seleção à procura de '\.jpg': 20

    return urls

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    # Verifica se o diretório informado já existe. Se não existir, cria-o.
    print('Criou dir?')
    print dest_dir

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print('sim')
    else:
        print ('nao')

    f_out = open(dest_dir + '/index.html', 'w')
    f_out.writelines(['<html>\n','<body>\n'])

    counter = 0
    for link in img_urls:
        urllib.urlretrieve(link, dest_dir + '/img' + str(counter))
        f_out.write('    <img src="img' + str(counter) + '">\n')
        counter += 1

    f_out.writelines(['</body>\n','</html>'])

    f_out.close()

    return


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
