form django import forms 
from .models import Contact

class ContactForm(forms.Form):
    """
    A form for the user to reach out to the admin
    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        
