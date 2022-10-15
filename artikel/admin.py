from django.contrib import admin
from artikel.models import Artikel


class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "update", "publish"]


admin.site.register(Artikel, ArtikelAdmin)
