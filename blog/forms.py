from .models import PostModel
from django import forms 



class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'title',
            'content'
        ]