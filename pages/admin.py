from re import search
from django.contrib import admin

# importamos nuestro modelo
from .models import Page

#configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    search_fields=('title', 'content')
    list_filter=('visible',)
    list_display=('title','visible','created_at')
    ordering=('created_at',)


#registramos nuestro modelo
admin.site.register(Page,PageAdmin)

#configuracion del panel
title="Proyecto Django"
subtitle="Panel de gestion"

admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle

