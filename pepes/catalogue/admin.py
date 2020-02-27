from django.contrib import admin
from django.utils.html import format_html
from .models import Pepe


class PepeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        print(obj.image.url)
        return format_html('<img src="{}" />'.format(obj.image.url))
    
    image_tag.short_description = 'Pepe'

    list_display = ['image_tag', ]

    
admin.site.register(Pepe, PepeAdmin)