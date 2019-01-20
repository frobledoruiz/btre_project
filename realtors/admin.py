from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('name', 'hire_date')
    list_editable = ('is_mvp',)
    search_fields = ('name', 'phone')
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
