import urllib2
url = 'http://127.0.0.1:8000/spider'
content = urllib2.urlopen(url)
print content.read()
