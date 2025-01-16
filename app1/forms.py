from django.forms import ModelForm
from .models import App1model

class App1Form(ModelForm):
    class Meta:
        model=App1model
        fields=['name','contact','address']