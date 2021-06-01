from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Dissertation(models.Model):
    dissertation_name = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.dissertation_name

    class Meta:
        verbose_name = 'Диссертация'
        verbose_name_plural = 'Диссертации'


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
    year_of_degree = models.IntegerField('Год получения степени', null=True,
                                         validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    university_id = models.ForeignKey(University, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    math_subject_class_id = models.ForeignKey(MathSubjectClass, on_delete=models.CASCADE)
    dissertation_id = models.ForeignKey(Dissertation, on_delete=models.CASCADE, null=True)

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

    def __str__(self):
        return '{0} - {1}'.format(self.student, self.advisor)

    class Meta:
        verbose_name = 'Студент-Науч'
        verbose_name_plural = 'Студенты-Научи'
        unique_together = (("student", "advisor"),)


class Article(models.Model):
    article_name = models.CharField('Название', max_length=200)
    year = models.IntegerField('Год написания статьи', null=True,
                               validators=[MinValueValidator(1900), MaxValueValidator(2023)])

    def __str__(self):
        return self.article_name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleMathematician(models.Model):
    article = models.ForeignKey(Article, related_name='articleMath', on_delete=models.CASCADE)
    mathematician = models.ForeignKey(Mathematician, related_name='mathematician', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}: {1}'.format(self.mathematician, self.article)

    class Meta:
        verbose_name = 'Статья-Математик'
        verbose_name_plural = 'Статьи-Математики'
        unique_together = (("article", "mathematician"),)


class Magazine(models.Model):
    magazine_name = models.CharField('Название', max_length=200)
    year = models.IntegerField('Год выпуска журнала', null=True,
                               validators=[MinValueValidator(1900), MaxValueValidator(2023)])

    def __str__(self):
        return self.magazine_name

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'


class MagazineArticle(models.Model):
    article = models.ForeignKey(Article, related_name='articleMag', on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, related_name='mathematician', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.magazine, self.article)

    class Meta:
        verbose_name = 'Статья-Журнал'
        verbose_name_plural = 'Статьи-Журналы'
        unique_together = (("article", "magazine"),)
