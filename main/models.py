from django.db import models
from django.urls import reverse


class University(models.Model):
    university_name = models.CharField('Название', max_length=80)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'


class Country(models.Model):
    country_name = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class MathSubjectClass(models.Model):
    math_subject_class_name = models.CharField('Название', max_length=80)

    def __str__(self):
        return self.math_subject_class_name

    class Meta:
        verbose_name = 'Предметный класс'
        verbose_name_plural = 'Предметные классы'


class Mathematician(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    middle_mane = models.CharField('Отчество', max_length=30, null=True)
    last_name = models.CharField('Фамилия', max_length=30)
    year_of_degree = models.IntegerField('Год получения степени', null=True)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    math_subject_class_id = models.ForeignKey(MathSubjectClass, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('math', kwargs={'math_id': self.pk})

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Математик'
        verbose_name_plural = 'Математики'


class StudentAdvisor(models.Model):
    student = models.ForeignKey(Mathematician, related_name='student', on_delete=models.CASCADE)
    advisor = models.ForeignKey(Mathematician, related_name='advisor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Студент-Науч'
        verbose_name_plural = 'Студенты-Научи'
        unique_together = (("student", "advisor"),)
