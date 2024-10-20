from django import forms
from . import User, Address, PhoneNumber, Profession, UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        labels = {
            'username': 'User name',
            'email'   : 'E-mail',
            'password': 'Password'
        }

        widgets  ={
            'username': forms.TextInput(attrs={'placeholder': 'JoseMaria'}),
            'email'   : forms.TextInput(attrs={'placeholder': 'jose.maria@gmail.com'}),
            'password': forms.TextInput(attrs={'placeholder': 'Senha'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

        labels = {
            'street'  : 'Street',
            'city'    : 'City',
            'state'   : 'State',
            'zip_code': 'Zip Code'
        }

        widgets  ={
            'street'  : forms.TextInput(attrs={'placeholder': 'Street'}),
            'city'    : forms.TextInput(attrs={'placeholder': 'City'}),
            'state'   : forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
        }

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

        labels = {
            'phone_number': 'Phone Number',
            'phone_type'  : 'Phone Type'
        }

        widgets  ={
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'phone_type'  : forms.TextInput(attrs={'placeholder': 'Phone Type'})
        }

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'

        labels = {
            'title'      : 'Profession Title',
            'description': 'Description'
        }

        widgets  ={
            'title'      : forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'description': forms.TextInput(attrs={'placeholder': 'Phone Type'})
        }

