from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # An instance is created when The form of page is displayed
        super().__init__(*args, **kwargs) # call basic class ModelForm
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields =['title', 'slug', 'content', 'photo', 'is_published', 'cat'] # which fields must be displayed in form(__all__ means all fields except autofilled)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #chenge html form for title
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}) # cols raw are html attributes
        }
    def clean_title(self): # validate-method must start with "clean_"
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title
    '''
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs ={'class': 'form-input'}), label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label='Контент')
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True) # checkbox (required=False(optional field))
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана") # drop-down list
    '''
class RegisterUserForm(UserCreationForm): # UserCreationForm is an embedded django form
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})) # overriding
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))# overriding
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))# overriding
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))# overriding

    class Meta:
        model = User #Embedded model 'auth_user'
        fields = ('username', 'email', 'password1', 'password2')
       # widgets are design of fields

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})) # widgets show how to display a current field on the site
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10}))
    captcha = CaptchaField()