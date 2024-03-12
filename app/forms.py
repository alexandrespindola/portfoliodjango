from django import forms
from app.models import Contact

class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'honeypot', 'captcha']

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if honeypot:
            raise forms.ValidationError('This field should be left blank.')
        return honeypot