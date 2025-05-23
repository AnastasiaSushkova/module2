from django.contrib import admin
from .models import Image, Category

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'age_limit')
    list_filter = ('categories',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
