from django.contrib import admin
from .models import Dica

class ListandoDicas(admin.ModelAdmin):
    list_display = ('id', 'nome_dica', 'categoria', 'onde_assistir', 'publicada')
    list_display_links = ('id', 'nome_dica')
    search_fields = ('nome_dica',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 2

admin.site.register(Dica, ListandoDicas)
