from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index ,name = 'index'),
    path('account/login/',views.user_login ,name = 'login'),
    path('projects/',views.projects ,name = 'projects'),
    path('contact/',views.contact ,name = 'contact'),
    # path('github',views.github ,name = 'github'),
    path('about/',views.about ,name = 'about'),
    
    
    
]