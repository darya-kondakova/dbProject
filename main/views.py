from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Mathematician, Country, University, MathSubjectClass, StudentAdvisor
from .forms import MathematicianForm, UserSignUpForm, UserSignInForm
from django.contrib.auth import login, logout
from django.db.models import Q
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

        maths = Mathematician.objects.all().order_by('-year_of_degree')

        if last_name is not None and middle_name is not None and first_name is not None and year_of_degree is not None and university is not None and country is not None and math_subject_class is not None:
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
                maths = maths.filter(country_id__country_name=country)
            if math_subject_class != '':
                maths = maths.filter(math_subject_class_id__math_subject_class_name__contains=math_subject_class)

        return maths


class MathDetailView(DetailView):
    model = Mathematician
    template_name = 'math_detail.html'
    pk_url_kwarg = 'math_id'

    def get_context_data(self, **kwargs):
        context = super(MathDetailView, self).get_context_data(**kwargs)
        context['students'] = Mathematician.objects.get(id=self.kwargs['math_id']).advisor.all()
        context['advisors'] = Mathematician.objects.get(id=self.kwargs['math_id']).student.all()
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
    return render(request, 'add.html', context)


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
