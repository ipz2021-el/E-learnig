from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('title',)
 
    def __str__(self):
        return self.title
 
class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('-created',)
 
    def __str__(self):
        return self.title
 
class Module(models.Model):
    course = models.ForeignKey(Course, 
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
 
    def __str__(self):
        return self.title

class ItemBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
 
class Text(ItemBase):
    content = models.TextField()
 
class File(ItemBase):
    file = models.FileField(upload_to='files')
 
class Image(ItemBase):
       file = models.FileField(upload_to='images')
 
class Video(ItemBase):
    url = models.URLField()