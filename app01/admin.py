from django.contrib import admin
from .models import Article
from .models import Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)