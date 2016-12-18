from django.contrib import admin
from .models import MyUser, Comment, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('kind', 'name', 'description', 'image', 'publisher', 'publish_time')

admin.site.register(Product, ProductAdmin)
admin.site.register(MyUser)