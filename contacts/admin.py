from django.contrib import admin
from . import models

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    list_display_links = ('id', 'first_name')
    list_per_page = 25


admin.site.register(models.Contact, ContactAdmin)
