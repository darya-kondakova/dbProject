from django.test import TestCase
from django.urls import reverse, resolve

from .models import Mathematician, Country, University, MathSubjectClass, StudentAdvisor
from django.contrib.auth import get_user_model
from .views import add, Search, MathDetailView

User = get_user_model()


class MathTestCases(TestCase):
    def setUp(self) -> None:
        self.country = Country.objects.create(country_name='testCountry')
        self.university = University.objects.create(university_name='testUniversityy')
        self.mathClass = MathSubjectClass.objects.create(math_subject_class_name='testMathClass')
        self.math = Mathematician.objects.create(
            last_name='testLast',
            middle_mane='testMiddle',
            first_name='testFirst',
            year_of_degree=1234,
            country_id=self.country,
            university_id=self.university,
            math_subject_class_id=self.mathClass
        )

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, add)

    def test_search_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, Search)

    def test_view_math_url_is_resolved(self):
        url = reverse('math', args=[1234])
        self.assertEquals(resolve(url).func.view_class, MathDetailView)

