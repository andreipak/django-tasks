from django.shortcuts import render
from django.template import RequestContext
from testassignment.logger.models import HttpRequestLogEntry


def requests(request, template='requests.html'):
    entries = HttpRequestLogEntry.objects.all().order_by('-date')[:10]
    return render(request, template, {'entries': entries})