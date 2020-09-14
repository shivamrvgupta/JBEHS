from django.contrib import admin
from .models import Result, Subject
# Register your models here.


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'std', 'total_marks', 'percentage')
    list_display_links = ('id', 'student')
    list_filter = ('std',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'subject_code',)
    list_display_links = ('id', 'subject')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Result, ResultAdmin)
