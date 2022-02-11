from enum import unique
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

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
    title = models.CharField(max_length=200,primary_key=True)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

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

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents',on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,limit_choices_to={'model__in':('text',
                                        'video',
                                        'image',
                                        'file')},on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']
    
class Quiz(models.Model):
    title = models.CharField(max_length=200,primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              related_name='quizes_created',
                              on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,
                    related_name = 'questions',
                    on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    answear = models.CharField(max_length=200)

class Option(models.Model):
    question = models.ForeignKey(Question,related_name = 'options',on_delete=models.CASCADE)
    text = models.CharField(max_length=200)