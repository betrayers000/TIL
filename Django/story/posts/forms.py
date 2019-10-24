from django import forms
from .models import Post, Comment, Image
from django.forms import inlineformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3)