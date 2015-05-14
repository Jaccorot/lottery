import urllib2
url = 'http://pailie3.sinaapp.com/spider'
content = urllib2.urlopen(url)
print content.read()
