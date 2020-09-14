from django.contrib import admin
from .models import Role, TeachersDetail, Teacher
# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role',)
    list_display_links = ('id', 'role')
    list_filter = ('role',)


admin.site.register(Role, RoleAdmin)


class TeachersDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',
                    'last_name', 'mobile_number')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'middle_name', 'last_name', 'mobile_number')


admin.site.register(TeachersDetail, TeachersDetailAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'teacher_code', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('first_name', 'middle_name', 'last_name', 'mobile_number')


admin.site.register(Teacher, TeacherAdmin)
