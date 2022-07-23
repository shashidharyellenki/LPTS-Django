from django.urls import  path
from . import views
urlpatterns=[
    path('Registrations/', views.Registrations, name='Registrations'),
    
]