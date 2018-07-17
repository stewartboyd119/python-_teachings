#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def read_urls(filename):

  #os.chdir("C:\\Users\\cr481e\\names")
  #full_path = os.path.abspath(os.path.join("./",filename))
  full_path = filename
  with open(full_path) as myfile:
      lines = myfile.readlines()
  jpglist = []
  for line in lines:
      search = re.findall(r"GET (\S+.jpg)",line)
      if search != []:
          jpglist += search
  undup_jpglist = list(set(jpglist))
  undup_jpglist.sort()
  return undup_jpglist


def download_images(img_urls, dest_path):
  if not os.path.exists(dest_path):
      os.makedirs(dest_path)
  domain_name = "http://code.google.com"
  for url in img_urls:
      address = domain_name + url
      contents = urllib2.urlopen(address).read()
      with open(os.path.join(dest_path, os.path.basename(address)),'wb') as myfile:
          myfile.write(contents)


  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  #main()
  #print(read_urls("animal_code.google.com"))
  download_images(read_urls("animal_code.google.com"), "./dog")