from django import forms
from .models import Product
from django.core.exceptions import ValidationError

forbid_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'created_at', 'last_changed_at']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in forbid_words:
            if word in name:
                raise ValidationError('Запрещённое слово в имени продукта')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in forbid_words:
            if word in description:
                raise ValidationError('Запрещённое слово в описании продукта')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выберите категорию'  # Текст подсказки внутри поля
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Дата в формате YYYY-MM-DD'  # Текст подсказки внутри поля
        })

        self.fields['last_changed_at'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Дата в формате YYYY-MM-DD'  # Текст подсказки внутри поля
        })
