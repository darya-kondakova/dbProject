from django.contrib import admin
from .models import Mathematician, MathSubjectClass, Country, University, StudentAdvisor


class MathematicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = [
        'id',
        'last_name',
    ]


admin.site.register(Mathematician, MathematicianAdmin)
admin.site.register(MathSubjectClass)
admin.site.register(Country)
admin.site.register(University)
admin.site.register(StudentAdvisor)


