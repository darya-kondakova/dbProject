from django.contrib import admin
from .models import Mathematician, MathSubjectClass, Country, University, StudentAdvisor, Dissertation, Article, \
    ArticleMathematician, Magazine, MagazineArticle


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
admin.site.register(Dissertation)
admin.site.register(Article)
admin.site.register(ArticleMathematician)
admin.site.register(Magazine)
admin.site.register(MagazineArticle)


