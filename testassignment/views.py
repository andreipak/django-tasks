from django.http import HttpResponse
from t1_contact.models import Contact, ContactForm

def home(request):
    aboutme = Contact.objects.get(pk=1)
    form = ContactForm(instance=aboutme)
    html = form.as_p()
    html = html.replace('id=', 'disabled="disabled" id=')
    return HttpResponse(html)
