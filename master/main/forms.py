from .models import *
from django.forms import ModelForm, TextInput, Textarea


class Forma(ModelForm):
    class Meta:
        model = Post_models
        fields = ['name', 'surname', 'father_name', 'num', 'email', 'roj', 'graj', 'region', 'programm', 'category', 'zan', 'reg_bezrab', 'obraz', 'galka']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'contact-form-lastname'
            }),
            'surname': TextInput(attrs={
                'placeholder': 'Фамилия',
                'class': 'contact-form-name'
            }),
            'father_name': TextInput(attrs={
                'placeholder': 'Отчество',
                'class': 'contact-form-type'
            }),
            'num': TextInput(attrs={
                'placeholder': 'Номер телефона',
                'class': 'contact-form-type'
            }),
            'email': TextInput(attrs={
            'placeholder': 'Email',
                'class': 'contact-form-type'
            }),
            'roj': TextInput(attrs={
                'placeholder': 'Дата рождения',
                'class': 'contact-form-type'
            }),
            'graj': TextInput(attrs={
                'placeholder': 'Гражданство',
                'class': 'contact-form-type'
            }),
            'region': TextInput(attrs={
                'placeholder': 'Регион',
                'class': 'contact-form-type'
            }),
            'programm': TextInput(attrs={
                'placeholder': 'Программа',
                'class': 'contact-form-type'
            }),
            'category': TextInput(attrs={
                'placeholder': 'Категория',
                'class': 'contact-form-type'
            }),
            'zan': TextInput(attrs={
                'placeholder': 'Занятость',
                'class': 'contact-form-type'
            }),
            'reg_bezrab': TextInput(attrs={
                'placeholder': 'Способ обратной связи',
                'class': 'contact-form-type'
            }),
            'obraz': TextInput(attrs={
                'placeholder': 'Образ',
                'class': 'contact-form-type'
            }),
        }