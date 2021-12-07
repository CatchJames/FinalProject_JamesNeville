from django import forms
from . models import MovieReview

class MovieReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = MovieReview
        fields = ['rating', 'review']
        widgets = {

        }


