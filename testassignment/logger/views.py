from django.shortcuts import render_to_response
from django.template import RequestContext
from testassignment.logger.models import HttpRequestLogEntry


def requests(request, template='requests.html'):
    entries = HttpRequestLogEntry.objects.all().order_by('-date')[:10]
    return render_to_response(template, {'entries': entries},
                                    context_instance=RequestContext(request))