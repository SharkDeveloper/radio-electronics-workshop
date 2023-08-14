from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='home'),
    path('about-us', views.about,name='about'),
    path('contact-us',views.contact_us, name='contact_us'),
    path('reviews',views.reviews, name='reviews'),
]