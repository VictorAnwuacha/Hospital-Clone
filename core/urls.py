from django.urls import path

app_name = 'core'

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/new/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:pk>/edit/', views.update_appointment, name='update_appointment'),
    path('appointments/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
    path('notifications/<int:patient_id>/', views.notification_list, name='notification_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

]

