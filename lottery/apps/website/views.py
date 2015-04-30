from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext


# Create your views here.


def index(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))
