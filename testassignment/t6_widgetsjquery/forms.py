from django.forms import ModelForm, Textarea
from testassignment.t1_contact.models import Contact
from testassignment.widgets import JQueryUIDatePickerWidget as DateWidget

from uni_form.helper import FormHelper
from uni_form.layout import Layout, Div, HTML, Submit

PHOTO_PREVIEW_TEMPLATE='''{% if contact.photo %}
<div id="photo-preview" style="background:url('{{ contact.photo.url }}')">
   <div id="photo-stub">Photo preview</div>
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
            'dateofbirth':DateWidget
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.form_id = 'contact_form'

        self.helper.layout = Layout(
            Div('name','lastname','dateofbirth','photo',
                    HTML(PHOTO_PREVIEW_TEMPLATE),
                    css_id='left'),

            Div('contacts','email','jabber','skype','othercontacts','bio',
                    css_id='right'),
            HTML('''<div class="clear"></div>
                    <input type="submit" name="save" value="Save" alt="Save changes" />
                    <a href="/" class="action" onclick="return confirm('Do you really want to cancel?')">Cancel</a>'''
            )

        )
        return super(ContactUniForm, self).__init__(*args, **kwargs)
