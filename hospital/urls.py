from django.urls import path
from . import views
urlpatterns = [
    path('test',views.test),
    path('index',views.index),
    path('about',views.about),
    path('treatment',views.treatment),
    path('contact',views.contact),
    path('doctor',views.doctor),
    path('signup',views.signup),
    path('sign',views.sign),
    path('login',views.login),
    path('bloodbank',views.bloodbank),
    path('log',views.log),
    path('apoint',views.apoint),
    path('donor',views.donor),
]
