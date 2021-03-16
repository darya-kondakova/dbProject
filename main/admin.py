from django.contrib import admin
from .models import Mathematician, MathSubjectClass, Country, University, StudentAdvisor

admin.site.register(Mathematician)
admin.site.register(MathSubjectClass)
admin.site.register(Country)
admin.site.register(University)
admin.site.register(StudentAdvisor)
