# -*- coding: utf-8 -*-
from django import forms
from models import User
from django.contrib.auth import authenticate
from captcha.fields import CaptchaField,CaptchaTextInput



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'required': ''}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль еще раз', 'required': ''}))
    username = forms.RegexField(label='', max_length=30,
        regex=r'^[\w.@+-]+$',
        widget=forms.TextInput(attrs={'placeholder': 'Логин', 'required': '', 'class': 'login', 'autocomplete': 'off'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'required': '', 'autocomplete': 'off'}))
    captcha = CaptchaField(label='', widget=CaptchaTextInput(attrs={'placeholder': 'Captcha', 'required': '', 'class': 'captcha', 'autocomplete': 'off'}))

    error_messages = {
        'invalid_login': ("Please enter a correct username and password. "
                           "Note that both fields are case-sensitive."),
        'no_cookies': ("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': ("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AuthenticationForm(forms.Form):
    email = forms.EmailField(label=("Email"), max_length=30)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': ("Please enter a correct username and password. "
                           "Note that both fields are case-sensitive."),
        'no_cookies': ("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': ("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
