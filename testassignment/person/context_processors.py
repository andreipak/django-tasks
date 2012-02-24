from django.conf import settings
from pprint import pformat

def projectsettings(request):
    return dict(settings=settings)


def projectsettings_dict(request):

    settings_dict = {}
    keys = [k for k in dir(settings) if k[0].isupper()]
    for k in keys:
        try:
            settings_dict[k] = pformat(getattr(settings, k, None))
        except:
            pass

    return dict(settings_dict=settings_dict)
