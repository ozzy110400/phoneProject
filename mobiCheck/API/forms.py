from django.forms import ModelForm
from .models import Phone


class NewPhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ('number',)
