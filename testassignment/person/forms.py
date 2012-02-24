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
            'other_contacts':Textarea({'cols':40, 'rows':10}),
            'dob':DateWidget
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(HTML(PHOTO_PREVIEW_TEMPLATE),
                'photo','dob','last_name','first_name',
                css_id='left'),

            Div('bio','other_contacts', 'skype', 'jabber', 'email',
                css_id='right'),

            HTML('<div class="clear"></div>'))

        return super(ContactUniForm, self).__init__(*args, **kwargs)
