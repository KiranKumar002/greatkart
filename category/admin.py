from django.contrib import admin
from .models import category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug'] #it prints before the table in the admin interface
admin.site.register(category,CategoryAdmin)
