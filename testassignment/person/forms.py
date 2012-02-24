from django.forms import ModelForm, Textarea
from models import Contact
from widgets import JQueryUIDatePickerWidget as DateWidget

from uni_form.helper import FormHelper
from uni_form.layout import Layout, Div, HTML

PHOTO_PREVIEW_TEMPLATE='''{% if contact.photo %}
<div id="photo-preview" style="background:url('{{ contact.photo.url }}') no-repeat">
{% else %}
<div id="photo-preview">
   <div id="photo-stub">No photo</div>
{% endif %}
</div>'''

class ContactUniForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'bio':Textarea({'cols':40, 'rows':10}),
            'othercontacts':Textarea({'cols':40, 'rows':10}),
            'dateofbirth':DateWidget()
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(HTML(PHOTO_PREVIEW_TEMPLATE),
                'photo','dateofbirth','lastname','name',
                css_id='left'),

            Div('bio','othercontacts', 'skype', 'jabber', 'email', 'contacts',
                css_id='right'),

            HTML('<div class="clear"></div>'))

        return super(ContactUniForm, self).__init__(*args, **kwargs)
