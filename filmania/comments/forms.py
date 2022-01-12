from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Comment', widget=forms.TextInput(attrs={'placeholder': 'Add comment'}))
    class Meta:
        model = Comment
        fields = (
            'body',
        )