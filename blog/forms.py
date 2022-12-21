from .models import Comment, Post
from django import forms
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content']
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%'}})
        }
