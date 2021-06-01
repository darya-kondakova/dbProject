from django.urls import path
from . import views

urlpatterns = [
    path('', views.Search.as_view(), name='home'),
    path('add/', views.add, name='add'),
    path('math/<int:math_id>/', views.MathDetailView.as_view(), name='math'),
    path('math/<int:math_id>/update/', views.MathUpdateView.as_view(), name='update'),
    path('math/<int:math_id>/delete/', views.MathDeleteView.as_view(), name='delete'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('find-all/', views.forms, name='find-all'),
    path('country/<int:country_id>/delete/', views.CountryDeleteView.as_view(), name='delete-country'),
    path('country/<int:country_id>/update/', views.CountryUpdateView.as_view(), name='update-country'),
    path('add-country/', views.CountryCreateView.as_view(), name='add-country'),
    path('university/<int:univ_id>/delete/', views.UniversityDeleteView.as_view(), name='delete-university'),
    path('university/<int:univ_id>/update/', views.UniversityUpdateView.as_view(), name='update-university'),
    path('add-university/', views.UniversityCreateView.as_view(), name='add-university'),
    path('math-sbj/<int:math_sbj_id>/delete/', views.MathClassDeleteView.as_view(), name='delete-math_sbj'),
    path('math_sbj/<int:math_sbj_id>/update/', views.MathClassUpdateView.as_view(), name='update-math_sbj'),
    path('add-math-sbj/', views.MathClassCreateView.as_view(), name='add-math_sbj'),
    path('st-ad/<int:st_ad_id>/delete/', views.StAdDeleteView.as_view(), name='delete-st_ad'),
    path('st-ad/<int:st_ad_id>/update/', views.StAdUpdateView.as_view(), name='update-st_ad'),
    path('add-st-ad/', views.StAdCreateView.as_view(), name='add-st_ad'),
    path('articles/', views.article, name='articles'),
]
