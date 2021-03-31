from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        # fields = ['title', 'body','author', 'image']

    def save(self, user):
        self.instance.author = user
        return super().save()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # if 'Hello' in title:
        #     raise forms.ValidationError("You  have a 'Hello' word in the title")
        if title[0].islower():
            raise forms.ValidationError("Сделай первую букву заглавной ;-)")
        return title

    def clean_body(self):
        body = self.cleaned_data.get('body')
        title = self.cleaned_data.get('title')
        if 'Источник:' not in body:
            raise forms.ValidationError("You must have a 'Источник:' word in the body")
        if  len(title) > len(body):
            raise forms.ValidationError("Название не может быть длинее поста")
        return body

    # def clean_body(self):
    #     if not 'Источник:' in self.data['body']:
    #         raise forms.ValidationError("Can't create post without 'Источник:'!")
    #     return self.body




    # def save(self, request=None):
    #     return super().save()

    # def save(self, request):
    #     return super().save(self, request)

    #
    # def post_author(self):
    #     self.data['author'] = Post.author

    # def clean_title(self):
    #     if not 'Python' in self.data['title']:
    #         raise forms.ValidationError("Can't create post without Python!")
    #     return title
    #
    #
    # def clean(self, **kwargs):
    #     return super().clean(**kwargs)
