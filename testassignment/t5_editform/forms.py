from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    lastname = forms.CharField(label='Last name', max_length=50)
    dateofbirth = forms.DateField(label='Date of birth')
    bio = forms.CharField(label='Bio', widget=forms.Textarea, max_length=10000)
    contacts = forms.CharField(label='Contacts', max_length=200)
    email = forms.EmailField(label='Email')
    jabber = forms.EmailField(label='Jabber ID')
    skype = forms.CharField(label='Skype ID', max_length=50)
    othercontacts = forms.CharField(label='Other contacts',widget=forms.Textarea, max_length=10000)
