from django.forms import ModelForm
from hobbies.models import Hobby

class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        exclude = ("users",)
