from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index ,name = 'index'),
    path('account/login/',views.user_login ,name = 'login'),
    path('projects/',views.projects ,name = 'projects'),
    # path('create_comment',views.create_comment ,name = 'create_comment'),
    
    
    
]