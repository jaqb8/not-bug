from django import forms
from django.forms.widgets import TextInput, Textarea
from posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "width: 300px",
            }
        )
    )
    content = forms.CharField(
        widget=Textarea(
            attrs={
                "rows": 5,
                "style": "width: 500px",
                "class": "form-control",
            }
        )
    )
