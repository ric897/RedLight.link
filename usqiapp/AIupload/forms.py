from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *












class Registration(UserCreationForm):
  email = forms.EmailField(max_length=60, label='BU Email Address', help_text='Required. Add a valid BU email address. Used to log in.')
  first_name = forms.CharField(max_length=20, label='Your Full Name')
  phone = forms.CharField(max_length=20, label='Your Phone (No +1, No Dashes or Paranthesis)', widget=forms.TextInput(attrs={'placeholder': 'Ex. 6173593510', 'type': 'tel'}))
  help_phone = forms.CharField(max_length=20, label='Emergency Contact Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Ex. 6173593510', 'type': 'tel'}))
  promo = forms.BooleanField(initial=True, label='',help_text='Agree to receive mental health resources and our community newsletter via text and/or email.', widget=forms.CheckboxInput(attrs={'label': 'Yo'}), required=False)
  #terms = forms.BooleanField(initial=True, label='',help_text="Agree to our <a class='underline' href='https://www.termsandconditionsgenerator.com/live.php?token=8B9ST0IO2FNS3dSXUGSL2sfdCbVg7oSP'> Terms and Conditions.</a> and <a class='underline' href='#'>Privacy Policy</a>", widget=forms.CheckboxInput(attrs={'label': 'Yo'}))


  def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        for fieldname in ['email','password1', 'password2']:
            self.fields[fieldname].help_text = None

  class Meta: 
    model = NewUser
    fields = ['email', 'first_name', 'phone', 'help_phone', 'password1', 'password2', 'promo']

    












        

        