from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    fields = (
        ('name', 'slug'),
    )

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fields = ('title', 'image',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'main_page')
    list_filter = ['main_page']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        ('pub_date', 'title', 'description', 'main_page'),
        ('text',),
        ('slug',),
    )

    def delete_file(self, pk, request):
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)