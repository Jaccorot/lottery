from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext

from lottery.apps.website.models import Num3D


# Create your views here.


def index(request):
    nums = Num3D.objects.all()
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
