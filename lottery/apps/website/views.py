from django.shortcuts import render, get_object_or_404, render_to_response
# from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.views import generic
# from django.utils import timezone
from django.template import RequestContext

import urllib2
import time

from bs4 import BeautifulSoup

from lottery.apps.website.models import Num3D


def index(request):
    nums = Num3D.objects.all()
    loop_times = [i for i in range(10)]
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))


def spider(request, year=""):
    try:
        status = ""
        spider_flag = 1
        if year == "":
            spider_flag = 0
            year = int(time.strftime("%Y", time.localtime()))
        get_data(year, spider_flag)
    except:
        status = "Failed"
    else:
        status = "Success"
    finally:
        return render_to_response("spider.html", {"status": status}, context_instance=RequestContext(request))


# def spider_all(request):
#     try:
#         status = ""
#         current_year = int(time.strftime("%Y", time.localtime()))
#         for i in range(2004, current_year + 1):
#             get_data(i, 1)
#     except:
#         status = "Failed"
#     else:
#         status = "Success"
#     finally:
#         return render_to_response("spider.html", {"status": status}, context_instance=RequestContext(request))


def get_data(year, is_all=1):
    current_year = str(year) + "-1-1"
    all_str = ""
    url = 'http://www.lecai.com/lottery/draw/list/3?d=' + current_year
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content, "html.parser")
    if not is_all:
        all_str = ":nth-of-type(1)"

    for i in soup.select("tbody > tr" + all_str):
        current_turn = int(i.select("td:nth-of-type(2) > a")[0].contents[0])
        current_num1 = int(i.select("td:nth-of-type(3) > span > span:nth-of-type(1)")[0].contents[0])
        current_num2 = int(i.select("td:nth-of-type(3) > span > span:nth-of-type(2)")[0].contents[0])
        current_num3 = int(i.select("td:nth-of-type(3) > span > span:nth-of-type(3)")[0].contents[0])
        db_temp = Num3D(turn=current_turn, num1=current_num1, num2=current_num2, num3=current_num3)
        db_temp.save()
