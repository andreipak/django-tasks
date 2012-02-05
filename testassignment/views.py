from django.template import loader, Context
from django.http import HttpResponse
from t1_contact.models import Contact
from t3_httplog.models import HttpRequestLogEntry
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from context_processors import projectsettings, projectsettings_dict
from django.contrib.auth.decorators import login_required
from t5_editform.forms import ContactForm


def index(request, template='index.html'):
    contact = get_object_or_404(Contact)

    return render_to_response(
                    template,
                    context_instance=RequestContext(
                        request,
                        {'contact':contact},
                        processors=[projectsettings]
                    ))

def edit(request, template_name='edit.html'):
    contact = get_object_or_404(Contact)

    form = ContactForm(initial=contact.__dict__)
    return render_to_response(
                    template_name,
                    context_instance=RequestContext(
                        request,
                        {'form':form, 'contact':contact}
                    ))



def settings(request, template='settings.html'):

    return render_to_response(
                    template,
                    context_instance=RequestContext(
                        request,
                        processors=[projectsettings_dict]
                    ))



def home(request):
    aboutme = Contact.objects.get(pk=1)
    t = loader.get_template('home.html')
    html = t.render(Context(dict(contact=aboutme)))
    return HttpResponse(html)


def requests(request):
    entries = HttpRequestLogEntry.objects.all().order_by('-date')[:10]
    t = loader.get_template('requests.html')
    html = t.render(Context(dict(entries=entries)))
    return HttpResponse(html)
