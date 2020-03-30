from django import forms
from .views import professors
from .models import reviews
class ReviewForm(forms.Form):
    rating = forms.IntegerField()
    comment = forms.CharField()
    anonymous=forms.NullBooleanField()
    class Meta:
        model=reviews

class ReviewUpdateForm(forms.Form):
    rating = forms.IntegerField()
    comment = forms.CharField()
    anonymous=forms.NullBooleanField()
    class Meta:
        model=reviews