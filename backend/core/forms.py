from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'body', 'image']
        fields = ['title', 'body', 'author', 'image']


    # def clean_title(self):
    #     if not 'Python' in self.data['title']:
    #         raise forms.ValidationError("Can't create post without Python!")
    #     return title
    #
    #
    # def clean(self, **kwargs):
    #     return super().clean(**kwargs)
