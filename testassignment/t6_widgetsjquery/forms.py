from django.forms import ModelForm, Textarea
from testassignment.t1_contact.models import Contact
from testassignment.widgets import JQueryUIDatePickerWidget as DateWidget

from uni_form.helper import FormHelper
from uni_form.layout import Layout, Div, HTML, Submit

class ContactUniForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'bio':Textarea({'cols':40, 'rows':10}),
            'othercontacts':Textarea({'cols':40, 'rows':10}),
            'dateofbirth':DateWidget
        }

        exclude = ('id', 'photo', 'contacts')



    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = ''
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div('name','lastname','dateofbirth','bio', css_id='left'),
            Div('email','jabber','skype','othercontacts', css_id='right'),
            HTML('''<div class="clear"></div>
                    <input type="submit" name="submit" value="Save" alt="Save changes" />
                    <a href="/" class="action" onclick="return confirm('Do you really want to cancel?')">Cancel</a>'''
            )

        )
        return super(ContactUniForm, self).__init__(*args, **kwargs)
