from django.contrib import admin
from .models import *

class Post(admin.ModelAdmin):
    list_display = ('surname', 'vremya', 'roj', 'region', 'programm''', 'category', 'zan', 'reg_bezrab', 'obraz', 'galka', 'vremya')
    list_display_links = ()
    search_fields = ('name', 'surname', 'father_name', 'roj')
    list_filter = ('zan', 'reg_bezrab', 'obraz', 'galka')
    list_editable = ('galka',)
    fields = ('name', 'surname', 'father_name', 'email', 'num', 'roj', 'graj', 'region', 'programm', 'category', 'zan', 'reg_bezrab', 'obraz', 'vremya')
    readonly_fields = ('vremya',)


class Catalog(admin.ModelAdmin):
    list_display = ('name', 'announce', 'date')
    list_display_links = ()
    search_fields = ()
    list_filter = ('date',)
    list_editable = ()
    fields = ('image_main', 'image3', 'image4', 'name', 'announce', 'discr1', 'discr2', 'discr3', 'discr4', 'discr5', 'osob', 'ysl', 'obyem', 'zanyatia', 'format', 'discr01', 'discr02', 'discr03', 'discr04', 'discr05', 'discr06', 'discr07', 'discr08')
    readonly_fields = ('date',)



admin.site.register(Post_models, Post)
admin.site.register(Catalog_models, Catalog)