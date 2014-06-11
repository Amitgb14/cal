#!/usr/bin/env python
import urllib2
url = "http://sourceforge.net/"
url_read = urllib2.urlopen(url)
print url_read.read()
