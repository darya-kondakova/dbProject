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
]
