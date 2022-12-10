from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ad, Profiles
from django.forms import ModelForm, TextInput, Select, NumberInput, Textarea
from django import forms


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['mark', 'model', 'age', 'body', 'shift', 'mileage', 'engine', 'volume', 'driveunit', 'vin', 'city',
                  'price', 'comment', 'image']

        widgets = {
            "mark": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: Lada'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 2107'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 2012'
            }),
            "body": Select(attrs={'class': 'form-select'}),

            "shift": Select(attrs={'class': 'form-select'}),

            "mileage": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 10500'
            }),

            "engine": Select(attrs={'class': 'form-select'}),
            "volume": Select(attrs={'class': 'form-select'}),
            "driveunit": Select(attrs={'class': 'form-select'}),

            "vin": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ZFA22300005556777'
            }),

            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Москва'
            }),

            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1 000 000 руб.'
            }),

            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий'
            }),
        }


class RegisterUserForm(UserCreationForm):
    uname = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Иванов Иван Иванович'}))

    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'name@email.ru'}))

    phone_number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': '+7 (ХХХ) ХХХ ХХ ХХ'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'password'}))

    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                         'placeholder': 'password'}))

    class Meta:
        model = Profiles
        fields = ['uname', 'email', 'phone_number', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'name@email.ru'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'password'}))


class UpdateUserForm(ModelForm):
    uname = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Иванов Иван Иванович'}))

    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'name@email.ru'}))

    phone_number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': '+7 (ХХХ) ХХХ ХХ ХХ'}))

    class Meta:
        model = Profiles
        fields = ['uname', 'email', 'phone_number']
