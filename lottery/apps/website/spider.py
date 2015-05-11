import urllib2

from bs4 import BeautifulSoup

from lottery.apps.website.models import Num3D


def catch_url(url):
    current_num = []
    url = 'http://cp.sogou.com/iframe/kaijiang/sohufragment/pl3/1.html'
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    current_turn = int(soup.select("option[selected]")[0].contents[0])
    for num_string in soup("i"):
        current_num.append(int(num_string.contents[0]))

    db_temp = Num3D(turn=current_turn, num1=current_num[0], num2=current_num[1], num3=current_num[2])
    db_temp.save()
