from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)