from django.shortcuts import render, get_object_or_404, render_to_response
# from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.views import generic
# from django.utils import timezone
from django.template import RequestContext

import urllib2

from bs4 import BeautifulSoup

from lottery.apps.website.models import Num3D


def index(request):
    nums = Num3D.objects.all()
    loop_times = [i for i in range(10)]
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))


def catch_url(request):
    try:
        current_num = []
        url = 'http://cp.sogou.com/iframe/kaijiang/sohufragment/pl3/1.html'
        content = urllib2.urlopen(url)
        soup = BeautifulSoup(content, "html.parser")
        current_turn = int(soup.select("option[selected]")[0].contents[0])
        for num_string in soup("i"):
            current_num.append(int(num_string.contents[0]))

        db_temp = Num3D(turn=current_turn, num1=current_num[0], num2=current_num[1], num3=current_num[2])
        db_temp.save()
        status = ""
    except:
        status = "Failed"
    else:
        status = "Success"
    finally:
        return render_to_response("spider.html", {"status": status}, context_instance=RequestContext(request))
