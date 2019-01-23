from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    search_fields = ('title', 'description', 'city', 'state', 'zipcode')
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
