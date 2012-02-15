from django import forms

class ContactForm(forms.Form):
    sender_name		= forms.CharField(max_length = 100)
    sender_email	= forms.EmailField()
    message			= forms.CharField(max_length = 2048, widget = forms.Textarea)