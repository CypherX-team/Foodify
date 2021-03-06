from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/about.html', views.about, name='about'),
    path('templates/contact.html', views.contact, name='contact'),
    path('templates/donate.html', views.donate, name='donate'),
    path('templates/recieve.html', views.recieve, name='recieve'),
    path('templates/signup.html', views.signup, name='signup')
]
