from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('single-service', single_service, name='single_service'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/project_details', project_details, name='project_details')
]