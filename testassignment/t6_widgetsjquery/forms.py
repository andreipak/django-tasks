from django.forms import ModelForm, Textarea
from t1_contact.models import Contact

from uni_form.helper import FormHelper
from uni_form.layout import Layout, Div, HTML, Submit


_html_actions = '''<div class="clear"></div>
<input type="submit" name="submit" value="Save" alt="Save changes" />
&nbsp;<a href="/" onclick="return confirm('Do you really want to cancel?')">Cancel</a>'''

class ContactUniForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'bio':Textarea({'cols':40, 'rows':10}),
            'othercontacts':Textarea({'cols':40, 'rows':10}),
        }

        exclude = ('id', 'photo', 'contacts')


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '/editmodel/'
        self.helper.form_method = 'POST'
        self.label_suffix = ":"
        #self.helper.form_style = 'inline'


        self.helper.layout = Layout(
            Div('name','lastname','dateofbirth','bio', css_id='left'),
            Div('email','jabber','skype','othercontacts', css_id='right'),
            HTML(_html_actions)
        )
        return super(ContactUniForm, self).__init__(*args, **kwargs)
