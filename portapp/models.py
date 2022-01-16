from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File


class Project(models.Model):
   
    title = models.CharField(max_length=50)
    image = CloudinaryField("image")
    description = models.TextField(max_length=600)
    technologies = models.TextField(max_length=100, null=True)
    url = models.URLField(null=True)
    link = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    
    @classmethod
    def search_project_name(cls, search_term):
        projects = cls.objects.filter(
        title__icontains=search_term)
        return projects    

    def str(self):
        return self.title

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class About(models.Model):
    description = models.TextField()
    image = CloudinaryField("image")
    skills = models.TextField()
    
    
    
    def __str__(self):
        return self.skills