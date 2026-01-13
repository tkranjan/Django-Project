from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','rating']
    search_fields = ['name']
    list_per_page = 10
    list_filter = ['rating']
admin.site.register(Product,ProductAdmin)

#class Meta:
    #ordering = ['created_at']