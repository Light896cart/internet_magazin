from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','get_html_photo','is_published','tags')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug':('title',)}

    def get_html_photo(self,objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width=50>")

# class ProductSizesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'product')
#     list_display_links = ('id', 'name', 'product')
#     search_fields = ('name','product')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub')
    list_display_links = ('id', 'sub')
    search_fields = ('sub',)
    prepopulated_fields = {'slug': ('sub',)}

# class SizeProductAdmin(admin.ModelAdmin):
#     list_display = ('id','clothing_size')
#     list_display_links = ('id','clothing_size')
#     search_fields = ('clothing_size',)

class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product,GoodsAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Category,CategoryAdmin)
# admin.site.register(ProductSizes,ProductSizesAdmin)
# admin.site.register(SizeProduct,SizeProductAdmin)
admin.site.register(Collections,CollectionsAdmin)
