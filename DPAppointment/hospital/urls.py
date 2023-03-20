from django.contrib import admin
from django.urls import path
from .views import About, Home, Contact, Login, Logout_admin, Index, View_doctor, Delete_doctor, Add_doctor, Add_patient, View_patient, Delete_patient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('add_doctor/', Add_doctor, name='add_doctor'),
    path('view_patient/', View_patient, name='view_patient'),
    path('add_patient/', Add_patient, name='add_patient'),
    path('delete_doctor(?p<int:pid>)/', Delete_doctor, name='delete_doctor'),
    path('delete_patient(?p<int:pid>)/', Delete_patient, name='delete_patient'),
]