from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('templates/index.html', views.index, name='index'),
    path('templates/about.html', views.about, name='about'),
    path('templates/contact.html', views.contact, name='contact'),
    path('templates/donate.html', views.donate, name='donate'),
    path('templates/receive.html', views.receive, name='receive'),
    path('templates/signup.html', views.signup, name='signup')
]
