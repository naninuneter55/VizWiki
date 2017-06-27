from django.contrib import admin
from .models import Material


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'template',)  # 一覧に出したい項目
    list_display_links = ('id', 'title',) 
admin.site.register(Material, MaterialAdmin)
