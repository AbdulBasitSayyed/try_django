from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.
admin.site.register(RecipeIngredient)

class RcipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields = ['name', 'quantity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines= [RcipeIngredientInline]
    list_display = ['name','user']
    readonly_fields= ['timestamp', 'updated']
    raw_id_fields= ['user']

admin.site.register(Recipe, RecipeAdmin)
