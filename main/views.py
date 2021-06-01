from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Mathematician, Country, University, MathSubjectClass, StudentAdvisor, ArticleMathematician, Article
from .forms import MathematicianForm, UserSignUpForm, UserSignInForm, CountryForm, MathSubjectClassForm, \
    UniversityForm, StudentAdvisorForm
from django.contrib.auth import login, logout
from django.db.models import Q, Count
import pandas as pd
import django.db.utils


# df = pd.read_csv('file.csv')
# for c in df['Country'].unique():
#     t = Country.objects.create(country_name=c)
#     t.save()
# for c in df['Univ'].unique():
#     t = University.objects.create(university_name=c)
#     t.save()
# for c in df.index:
# names = df.loc[c]['Name'].split()
#     if len(names) > 2:
#         fn = names[0]
#         mn = names[1]
#         ln = ' '.join(names[2:])
#     if len(names) == 2:
#         fn = names[0]
#         mn = None
#         ln = names[1]
#     user_id = df.loc[c]['id']
#     adv = df.loc[c]['Advisor'].replace('[', '').replace(']', '').replace("'", '').strip().split(', ')
#     for a in adv:
#         s = Mathematician.objects.get(id=user_id)
#         try:
#             aa = Mathematician.objects.get(id=a)
#             if aa:
#                 try:
#                     t = StudentAdvisor.objects.create(advisor=aa, student=s)
#                     t.save()
#                 except django.db.utils.IntegrityError:
#                     pass
#         except Exception:
#             pass
#     user_id = df.loc[c]['id']
#     adv = df.loc[c]['Students'].replace('[', '').replace(']', '').replace("'", '').strip().split(', ')
#     for a in adv:
#         aa = Mathematician.objects.get(id=user_id)
#         try:
#             s = Mathematician.objects.get(id=a)
#             t = StudentAdvisor.objects.create(advisor=aa, student=s)
#             t.save()
#         except Exception:
#             pass
#     if pd.isna(df.loc[c]['Year']):
#         year = None
#     else:
#         year = pd.to_numeric(df.loc[c]['Year'].split(',')[0])
#     univ = University.objects.get(university_name=df.loc[c]['Univ'])
#     math = MathSubjectClass.objects.all()[0]
#     country = Country.objects.get(country_name=df.loc[c]['Country'])
#     u = Mathematician.objects.create(id=user_id, first_name=fn, middle_mane=mn, last_name=ln,
#                                  year_of_degree=year, university_id=univ,
#                                  country_id=country,math_subject_class_id=math)
#     print(u)


class Search(ListView):
    model = Mathematician
    paginate_by = 19
    template_name = 'index.html'
    context_object_name = 'maths'

    def get_queryset(self):
        last_name = self.request.GET.get('last_name')
        middle_name = self.request.GET.get('middle_name')
        first_name = self.request.GET.get('first_name')
        year_of_degree = self.request.GET.get('year_of_degree')
        university = self.request.GET.get('university')
        country = self.request.GET.get('country')
        math_subject_class = self.request.GET.get('math_subject_class')
        order = self.request.GET.get('order')

        if order is not None and order != '':
            maths = Mathematician.objects.all().order_by(order)
        else:
            maths = Mathematician.objects.all().order_by('-year_of_degree')

        if last_name is not None and middle_name is not None and first_name is not None and year_of_degree is not None \
                and university is not None and country is not None and math_subject_class is not None and order is not None:
            if last_name != '':
                maths = maths.filter(last_name__contains=last_name)
            if middle_name != '':
                maths = maths.filter(middle_mane__contains=middle_name)
            if first_name != '':
                maths = maths.filter(first_name__contains=first_name)
            if year_of_degree != '':
                maths = maths.filter(year_of_degree=year_of_degree)
            if university != '':
                maths = maths.filter(university_id__university_name__contains=university)
            if country != '':
                maths = maths.filter(country_id__country_name__contains=country)
            if math_subject_class != '':
                maths = maths.filter(math_subject_class_id__math_subject_class_name__contains=math_subject_class)
            # if order != '':
            #     maths.order_by(order)
            # else:
            #     maths.order_by('-year_of_degree')

        return maths


class MathDetailView(DetailView):
    model = Mathematician
    template_name = 'math_detail.html'
    pk_url_kwarg = 'math_id'

    def get_context_data(self, **kwargs):
        context = super(MathDetailView, self).get_context_data(**kwargs)
        context['students'] = Mathematician.objects.get(id=self.kwargs['math_id']).advisor.all()
        context['advisors'] = Mathematician.objects.get(id=self.kwargs['math_id']).student.all()
        context['articles'] = ArticleMathematician.objects.values('mathematician').\
            filter(mathematician=self.kwargs['math_id']).annotate(total=Count('article'))
        context['form'] = MathematicianForm()
        return context


class MathUpdateView(UpdateView):
    model = Mathematician
    template_name = 'math_update.html'
    pk_url_kwarg = 'math_id'
    form_class = MathematicianForm


class MathDeleteView(DeleteView):
    model = Mathematician
    success_url = '/'
    template_name = 'math_delete.html'
    pk_url_kwarg = 'math_id'


def add(request):
    if request.method == 'POST':
        form = MathematicianForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
        else:
            return redirect('sign-in')

    form = MathematicianForm()
    context = {'form': form}
    return render(request, 'math_add.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = UserSignUpForm()
    context = {'form': form}
    return render(request, 'sign-up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    form = UserSignInForm()
    context = {'form': form}
    return render(request, 'sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('sign-in')


def forms(request):
    name = request.GET.get('name')

    countries = Country.objects.all().order_by('country_name')
    universities = University.objects.all()
    math_classes = MathSubjectClass.objects.all()
    student_advisor = StudentAdvisor.objects.all()

    if name is not None:
        countries = Country.objects.filter(country_name__contains=name).order_by('country_name')
        universities = universities.filter(university_name__contains=name)
        math_classes = math_classes.filter(math_subject_class_name__contains=name)
        student_advisor = student_advisor.filter(Q(student__last_name__contains=name) |
                                                 Q(student__middle_mane__contains=name) |
                                                 Q(student__first_name__contains=name) |
                                                 Q(advisor__last_name__contains=name) |
                                                 Q(advisor__middle_mane__contains=name) |
                                                 Q(advisor__first_name__contains=name))

    context = {'cs': countries, 'us': universities, 'ms': math_classes, 'sas': student_advisor}

    return render(request, 'find-all.html', context)


class CountryDeleteView(DeleteView):
    model = Country
    success_url = '/find-all'
    template_name = 'delete.html'
    pk_url_kwarg = 'country_id'


class CountryUpdateView(UpdateView):
    model = Country
    success_url = '/find-all'
    template_name = 'update.html'
    pk_url_kwarg = 'country_id'
    form_class = CountryForm


class CountryCreateView(CreateView):
    model = Country
    success_url = '/find-all'
    template_name = 'add.html'
    form_class = CountryForm


class UniversityDeleteView(DeleteView):
    model = University
    success_url = '/find-all'
    template_name = 'delete.html'
    pk_url_kwarg = 'univ_id'


class UniversityUpdateView(UpdateView):
    model = University
    success_url = '/find-all'
    template_name = 'update.html'
    pk_url_kwarg = 'univ_id'
    form_class = UniversityForm


class UniversityCreateView(CreateView):
    model = University
    success_url = '/find-all'
    template_name = 'add.html'
    form_class = UniversityForm


class MathClassDeleteView(DeleteView):
    model = MathSubjectClass
    success_url = '/find-all'
    template_name = 'delete.html'
    pk_url_kwarg = 'math_sbj_id'


class MathClassUpdateView(UpdateView):
    model = MathSubjectClass
    success_url = '/find-all'
    template_name = 'update.html'
    pk_url_kwarg = 'math_sbj_id'
    form_class = MathSubjectClassForm


class MathClassCreateView(CreateView):
    model = MathSubjectClass
    success_url = '/find-all'
    template_name = 'add.html'
    form_class = MathSubjectClassForm


class StAdDeleteView(DeleteView):
    model = StudentAdvisor
    success_url = '/find-all'
    template_name = 'delete.html'
    pk_url_kwarg = 'st_ad_id'


class StAdUpdateView(UpdateView):
    model = StudentAdvisor
    success_url = '/find-all'
    template_name = 'update.html'
    pk_url_kwarg = 'st_ad_id'
    form_class = StudentAdvisorForm


class StAdCreateView(CreateView):
    model = StudentAdvisor
    success_url = '/find-all'
    template_name = 'add.html'
    form_class = StudentAdvisorForm


def article(request):
    top = ArticleMathematician.objects.values('mathematician__last_name', 'mathematician__first_name').annotate(
        total=Count('article')).order_by('-total')[:3]

    having = ArticleMathematician.objects.values('mathematician__last_name', 'mathematician__first_name').annotate(
        total=Count('article')).filter(total__gt=2)

    articles = ArticleMathematician.objects.values('mathematician__last_name', 'mathematician__first_name').annotate(total=Count('article'))

    # out = Mathematician.objects.raw('SELECT mathematician_id as id, last_name, first_name, COUNT ("article") as total FROM '
    #                                 'main_mathematician OUTER JOIN main_articleMathematician GROUP BY mathematician_id HAVING total > 2 ')

    context = {'art': articles, 'having': having, 'top': top}
    return render(request, 'articles.html', context)
