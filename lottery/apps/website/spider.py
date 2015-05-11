import urllib2

from bs4 import BeautifulSoup


def catch_url(url):
    this_turn = []
    url = 'http://cp.sogou.com/iframe/kaijiang/sohufragment/pl3/1.html'
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    turn = int(soup.select("option[selected]")[0].contents[0])
    this_turn.append(turn)
    for num_string in soup("i"):
        this_turn.append(int(num_string.contents[0]))
#    print this_turn
