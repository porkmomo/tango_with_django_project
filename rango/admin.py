from django.contrib import admin
from rango.models import Category, Page

# Customize page admin to show more columns
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Customize Category admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register the models with their respective customised Admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)