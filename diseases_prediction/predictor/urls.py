from django.urls import path
from . import views
from .views import diabetes_profile, register, user_login, user_logout, heart_disease_profile, delete_heartdisease_data,delete_diabetes_data


urlpatterns = [
    path('admin/', views.admin_page, name='admin_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('index/', views.index_page, name='index_page'),
    path('heart/', views.heart_disease_prediction, name='heart_disease_prediction'),
    path('diabetes/', views.diabetes_prediction, name='diabetes_prediction'),
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('heart_disease_profile/', heart_disease_profile, name='heart_disease_profile'),
    path('diabetes_profile/', diabetes_profile, name='diabetes_profile'),
    path('heartdisease/delete/<int:pk>/', delete_heartdisease_data, name='delete_heartdisease_data'),
    path('diabetes/delete/<int:pk>/', delete_diabetes_data, name='delete_diabetes_data'),

]
