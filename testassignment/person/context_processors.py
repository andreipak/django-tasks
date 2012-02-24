from django.conf import settings

def projectsettings(request):
    return {'SETTINGS': settings}
