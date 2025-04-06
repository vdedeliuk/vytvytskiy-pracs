from django import forms
from .models import ArticleImage, Article

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = ArticleImage
        fields = ['article', 'image', 'title']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'text', 'pub_date', 'main_page']