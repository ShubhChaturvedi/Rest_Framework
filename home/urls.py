
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('update/<int:pk>/', views.update, name='update'),
    path('partial_update/<int:pk>/', views.partial_update, name='partial_update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('get_book/', views.get_book, name='get_book'),
    path('student_api/', views.StudentView.as_view() , name='student_api'),
]