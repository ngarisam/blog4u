from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
import random
class ReaderLoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Passsword',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ReaderRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Passsword',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

    # Generate random numbers for the math challenge
    num1 = random.randint(40, 80)
    num2 = random.randint(5, 20)

    # Randomly select whether to use addition or subtraction
    operation = random.choice(['+', '-'])

    if operation == '+':
        # Calculate the correct answer for addition
        correct_answer = num1 + num2
        challenge_label = f'What is {num1} + {num2}?'
    else:
        # Calculate the correct answer for subtraction
        correct_answer = num1 - num2
        challenge_label = f'What is {num1} - {num2}?'

    math_challenge = forms.IntegerField(
        label=challenge_label,
        error_messages={'invalid': 'Incorrect answer. Please try again.'}
    )

    def clean_math_challenge(self):
        math_challenge = self.cleaned_data['math_challenge']
        if math_challenge != self.correct_answer:
            raise forms.ValidationError('Incorrect answer. Please try again.')
        return math_challenge        