from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django import template
#from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

register = template.Library
# Create your models here


class Group(models.Model):
    '''
    This will initialize a class which will be called
    whenever a new group object is created
    '''
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    location = models.TextField(default='', blank=True)
    location_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        '''
        This is a string representation
        of the group object
        '''
        return self.name

    def save(self, *args, **kwargs):
        '''
        A function to save each group object
        '''
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def delete_Group(self, *args, **kwargs):
        '''
        A function to delete each group object
        '''
        self .slug = slugify(self.name)
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        '''
        A function which generates a unique url for each group
        '''
        return reverse('groups:single', kwargs={'slug': self.slug})

    @classmethod
    def search_by_name(cls, search_term):
        name = cls.objects.filter(name__icontains=search_term)
        return name

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    '''
    This will initialize a group member  class
    which is instiantiated whenever a group member object is created
    '''
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
