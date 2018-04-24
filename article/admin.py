from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_time', 'last_updated_time')
    ordering = ('id',)


admin.site.register(Article, ArticleAdmin)