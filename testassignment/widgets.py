from django import forms
from django.conf import settings

JDPICKER_MEDIA_PREFIX = getattr(settings, 'JDPICKER_MEDIA_PREFIX', None) or \
                        settings.STATIC_URL + 'jdpicker/'

JQUERYUI_MEDIA_PREFIX = getattr(settings, 'JQUERYUI_MEDIA_PREFIX', None) or \
                        settings.STATIC_URL


class JDPickerWidget(forms.widgets.DateInput):
    class Media:
        css = {'all':(JDPICKER_MEDIA_PREFIX + 'jdpicker.css',)}
        js = (JDPICKER_MEDIA_PREFIX + 'jquery.jdpicker.js',)

    def __init__(self, attrs={'class' : 'datepicker'}):
        super(JDPickerWidget, self).__init__(attrs=attrs)


class JQueryUIDatePickerWidget(forms.widgets.DateInput):
    class Media:
        css = {'all':(JQUERYUI_MEDIA_PREFIX + 'css/smoothness/jquery-ui-1.8.17.custom.css',)}
        js = (JQUERYUI_MEDIA_PREFIX + 'js/jquery-ui-1.8.17.custom.min.js', )

    def __init__(self, attrs={'class' : 'datepicker'}):
        super(JQueryUIDatePickerWidget, self).__init__(attrs=attrs)
