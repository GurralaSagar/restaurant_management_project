from django import forms
from .models import Feedback
from .models import ContactSubmission

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment' : forms.Textarea(attrs={
                'rows':5,
                'placeholder':'Write your feedback here...',
                'class':'form-control'
            })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email']