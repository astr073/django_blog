from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug may not be create')
        #
        # if Tag.objects.filter(slug__iexact=new_slug).count():
        #     raise ValidationError('this slug is already used')

        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
    #     return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('slug may not be create')
        return new_slug
