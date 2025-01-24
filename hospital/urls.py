from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('doctor_panel/', views.doctor_panel, name='doctor_panel'),
    path('update_appointment_status/<int:appointment_id>/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
]