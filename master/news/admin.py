from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class Novosti(admin.ModelAdmin):
    list_display = ('name', 'announce', 'date')
    list_display_links = ()
    search_fields = ()
    list_filter = ('name', 'date',)
    list_editable = ()
    fields = ('image', 'name', 'announce', 'full', 'source')
    readonly_fields = ('date',)

    def foto(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100")

admin.site.register(Novosti_models, Novosti)