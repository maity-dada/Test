from django.contrib import admin
from .models import *
# Register your models here.

class servicesAdmin(admin.ModelAdmin):
    list_display=('id','recipeName','recipeDescription','recipeImage','recipeImageUrl')
admin.site.register(recipe_module,servicesAdmin)   