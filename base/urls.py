from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="index"),
    path('about/' , views.aboutPage, name="about"),
    path('contact/' , views.contactPage, name="contact"),
    path('gallery/' , views.galleryPage, name="gallery"),
    path('profile/<str:pk>/' , views.profilePage, name="profile"),
    path('projects/' , views.projectsPage, name="projects"),
    path('services/' , views.servicesPage, name="services"),
    path('project/<str:pk>/' , views.projectPage, name="project"),
    path('service/<str:pk>/' , views.servicePage, name="service"),
    path('team/', views.teamPage, name="team"),
    path('search/', views.searchPage, name="search"),

]