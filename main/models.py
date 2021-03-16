from django.db import models


class University(models.Model):
    university_name = models.CharField('Название', max_length=80)


class Country(models.Model):
    country_name = models.CharField('Название', max_length=30)


class MathSubjectClass(models.Model):
    math_subject_class_name = models.CharField('Название', max_length=80)


class Mathematician(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    middle_mane = models.CharField('Отчество', max_length=30, null=True)
    last_name = models.CharField('Фамилия', max_length=30)
    year_of_degree = models.IntegerField('Год получения степени')
    university_id = models.ForeignKey(University, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    math_subject_class_id = models.ForeignKey(MathSubjectClass, on_delete=models.CASCADE)


class StudentAdvisor(models.Model):
    student = models.ForeignKey(Mathematician, related_name='student', on_delete=models.CASCADE)
    advisor = models.ForeignKey(Mathematician, related_name='advisor', on_delete=models.CASCADE)

    class Meta:
        unique_together = (("student", "advisor"),)

