from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, PasswordInput, CharField, EmailField, \
    EmailInput, ImageField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput, Textarea, FileInput
from register.models import Profile


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = {'password1', 'password2', 'email', 'username'}

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img', 'bio']

        widgets = {
            'profile_img': FileInput(attrs={
                'class': 'form-control',
            }),
            'bio': Textarea(attrs={
                'class': 'form-control bio',
                'placeholder': 'Расскажите о себе',
            }), }





class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = {'password', 'username'}

