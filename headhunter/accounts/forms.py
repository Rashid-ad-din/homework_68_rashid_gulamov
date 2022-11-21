from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput
from accounts.models import Account


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Имя'
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password'
        )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = (
            'usertype',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_confirm',
            'phone',
            'avatar'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')
        email = cleaned_data.get('email')
        if not email:
            raise ValidationError('Поле "Email" обязательно к заполнению')
        phone = cleaned_data.get('phone')
        if not phone:
            raise ValidationError('Поле "Телефон" обязательно к заполнению')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar'
        )


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    old_password = forms.CharField(
        label="Старый пароль",
        strip=False,
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неверный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']
#
#
# class SearchForm(forms.Form):
#     search = forms.CharField(max_length=100, required=False, label='', widget=TextInput(attrs={
#         'class': 'mr-3 ps-3 class-form border-0 border-top bg-light rounded',
#         'style': 'width: 270px; height: 35px; outline:0px none transparent; overflow:auto; resize:none',
#         'placeholder': 'Поиск',
#     }
#     ))
