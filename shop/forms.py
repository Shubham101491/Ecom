from django import forms
from shop.models import Watch

class WatchForm(forms.ModelForm):

    class Meta:
        model = Watch
        fields = "__all__"