from django.forms import ModelForm
from .models import Categories

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        