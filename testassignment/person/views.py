from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as _logout

from testassignment.person.models import Contact
from testassignment.logger.models import HttpRequestLogEntry
from forms import ContactUniForm as ContactForm

from testassignment.person.context_processors import projectsettings, projectsettings_dict


def index(request, template='index.html'):
    contact = get_object_or_404(Contact)

    return render_to_response(template, context_instance=RequestContext(
                        request, {'contact':contact}, processors=[projectsettings]))

@login_required
def edit(request, template_name='edit.html'):

    contact = get_object_or_404(Contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        if request.POST.get('is_ajaxForm') == '1':
            if form.is_valid():
                form.save()
                #hack for rendering "photo-clear" input
                form = ContactForm(instance=contact)

            return render_to_response('contact_form.html', {
                            'form':form, 'contact':contact
                        }, context_instance=RequestContext(request))

        if form.is_valid():
            form.save()
            return redirect('index')

        return render_to_response(template_name, {
                    'form':form, 'contact':contact
                }, context_instance=RequestContext(request))

    #GET request
    form = ContactForm(instance=contact)

    return render_to_response(template_name, {
                'form':form, 'contact':contact
            }, context_instance=RequestContext(request))


def settings(request, template='settings.html'):

    return render_to_response(template, context_instance=RequestContext(
                                request, processors=[projectsettings_dict]))


def logout(request):
    _logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))
