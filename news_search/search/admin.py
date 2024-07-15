from django.contrib import admin
from .models import Search, SearchResult

class SearchResultInline(admin.TabularInline):
    model = SearchResult

class SearchAdmin(admin.ModelAdmin):
    inlines = [SearchResultInline]

admin.site.register(Search, SearchAdmin)
admin.site.register(SearchResult)
