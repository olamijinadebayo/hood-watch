from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    '''
    This will initialize post model which will be instiantiated
    whenever a user creates a post
    '''
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    business_name = models.TextField()
    business_name_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        '''
        This will ensure that each post is displayed based on the message
        in the admin panel
        '''
        return self.message

    def save(self, *args, **kwargs):
        '''
        this save each post object for each user
        '''
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        '''
        This will generate a unique url for each group mem
        '''
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'business_name']
