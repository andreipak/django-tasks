from django.conf import settings

def projectsettings(request):
    return dict(settings=settings)
