from django.urls import path
from . import views

app_name = 'fatima_portfolio'
urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("resume/", views.resume, name='resume')
]