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
