from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about'),
    path('edit/<int:person_id>/', views.edit, name='edit'),   
    path('delete/<int:person_id>/', views.delete, name='delete'),
    path('department/', views.department_list, name='department_list'), 
]   