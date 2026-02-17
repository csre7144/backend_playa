from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('compounding/', views.compounding, name="compounding"),
    path('provider/', views.provider, name="provider"),
    path('transfer/', views.transfer, name="transfer"),
    path('contact/', views.contact, name="contact"),
    path('methylene/', views.methylene, name="methylene"),
    path('pain_management/', views.pain_management, name="pain_management"),
    path('hormone/', views.hormone, name="hormone"),
    path('sleep_aids/', views.sleep_aids, name="sleep_aids"),
    path('weight_management/', views.weight_management, name="weight_management"),
    path('pet_medicine/', views.pet_medicine, name="pet_medicine"),
    path('nutriceuticals/', views.nutriceuticals, name="nutriceuticals"),
    path('adrenal_fatigue/', views.adrenal_fatigue, name="adrenal_fatigue"),
    path('dermatology/', views.dermatology, name="dermatology"),
    path('additional_expertise/', views.additional_expertise, name="additional_expertise"),

    # Dashbaord Backend
    path('dashboard_admin/', views.dashboard, name="dashboard"),
    path('dashboard_admin/request_call/', views.request_call, name="request_call"),
    path('request_call/edit/<int:pk>/', views.edit_request_call, name='edit_request_call'),
    path('delete-request/<int:pk>/', views.delete_request_call, name='delete_request_call'),
    path('dashboard_admin/add-request/', views.add_request_call, name='add_request_call'),
    path('dashboard_admin/task_management', views.task_management, name="task_management"),
    path('dashboard_admin/contact_information', views.contact_information, name="contact_information"),
    path('dashboard_admin/contact_form', views.contact_form, name="contact_form"),
    path('dashboard_admin/transfer_rx', views.transfer_rx, name="transfer_rx"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)