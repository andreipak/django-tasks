from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as _logout
from testassignment.person.models import Contact
from testassignment.logger.models import HttpRequestLogEntry
from forms import ContactUniForm as ContactForm
from django.conf import settings

def index(request, template='index.html'):
    contact = get_object_or_404(Contact)

    return render(request, template, {'contact': contact})

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

            return render(request, 'contact_form.html', {'form':form, 'contact':contact})

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, template_name, {'form':form, 'contact':contact})

    #GET request
    form = ContactForm(instance=contact)

    return render(request, template_name, {'form':form, 'contact':contact})

def logout(request):
    _logout(request)
    return redirect('index')
