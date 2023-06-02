from django.contrib import admin
from .models import Photos, Category

# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Category, CategoryAdmin)
