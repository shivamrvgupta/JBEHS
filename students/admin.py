from django.contrib import admin
from .models import Student, StudentDetail, Photo

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',
                    'last_name', 'student_code', 'is_active')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'middle_name', 'last_name', 'mobile_number')
    list_filter = ('is_active',)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_code',
                    'mothers_name', 'student_aadhar_number')
    list_display_links = ('id', 'student_code')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname',)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail, DetailAdmin)
admin.site.register(Photo, PhotoAdmin)
