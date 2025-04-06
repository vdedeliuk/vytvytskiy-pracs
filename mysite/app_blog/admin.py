from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)  # Fixed: Changed 'category' to 'name'
    prepopulated_fields = {'slug': ('name',)}  # Fixed: Changed 'category' to 'name'
    fields = (
        ('name', 'slug'),  # Fixed: Changed 'category' to 'name'
    )

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fields = ('title', 'image',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    list_filter = ['main_page']
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fields = (
        ('pub_date', 'title', 'description', 'main_page'),
        ('category',),
        ('text',),
        ('slug',),  
    )

    def delete_file(self, pk, request):
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)