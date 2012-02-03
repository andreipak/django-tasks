from django.template import loader, Context
from django.http import HttpResponse
from t1_contact.models import Contact, ContactForm
from t3_httplog.models import HttpRequestLogEntry


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
