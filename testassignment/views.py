from django.template import loader, Context
from django.http import HttpResponse
from t1_contact.models import Contact
from t3_httplog.models import HttpRequestLogEntry
from django.shortcuts import get_object_or_404, render_to_response,  redirect
from django.template import RequestContext
from context_processors import projectsettings, projectsettings_dict
from django.contrib.auth.decorators import login_required
from t5_editform.forms import ContactForm
from django.contrib.auth import logout as _logout
from django.forms.models import model_to_dict


def index(request, template='index.html'):
    contact = get_object_or_404(Contact)

    return render_to_response(
                    template,
                    context_instance=RequestContext(
                        request,
                        {'contact':contact},
                        processors=[projectsettings]
                    ))

@login_required
def edit(request, template_name='edit.html'):

    contact = get_object_or_404(Contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.lastname = form.cleaned_data['lastname']
            contact.dateofbirth = form.cleaned_data['dateofbirth']
            contact.bio = form.cleaned_data['bio']
            contact.contacts = form.cleaned_data['contacts']
            contact.email = form.cleaned_data['email']
            contact.jabber = form.cleaned_data['jabber']
            contact.skype = form.cleaned_data['skype']
            contact.othercontacts = form.cleaned_data['othercontacts']

            if form.cleaned_data['photo']:
                contact.photo = form.cleaned_data['photo']
            elif request.POST.get('photo-clear') == 'on': #clear checkbox
                    contact.photo = None #fixme: handle removing from fs


            contact.save()

            return redirect('/')

        else:
            return render_to_response(
                    template_name,
                    context_instance=RequestContext(
                        request,
                        {'form':form, 'contact':contact}
                    ))




    form = ContactForm(initial=model_to_dict(contact))

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


def requests(request):
    entries = HttpRequestLogEntry.objects.all().order_by('-date')[:10]
    t = loader.get_template('requests.html')
    html = t.render(Context(dict(entries=entries)))
    return HttpResponse(html)


def logout(request):
    _logout(request)
    return redirect(request.META.get('HTTP_REFERER','/'))
