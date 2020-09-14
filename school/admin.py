from django.contrib import admin
from .models import School, Class
# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school_code')
    list_display_links = ('id', 'name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'std', 'class_teacher')
    list_display_links = ('id', 'std',)


admin.site.register(School, SchoolAdmin)
admin.site.register(Class, ClassAdmin)
