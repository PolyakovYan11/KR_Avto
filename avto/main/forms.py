from .models import Ad
from django.forms import ModelForm, TextInput, Select, NumberInput, Textarea


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['mark', 'model', 'age', 'body', 'shift', 'mileage', 'engine', 'volume', 'driveunit', 'vin', 'city',
                  'price', 'comment']

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
                'class': 'form-label',
                'placeholder': 'Ваш комментарий'
            })
        }
