from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.


class SignUp(CreateView):
    '''
    This will initialize a user sign up form using the create view class
    inherited from django's class based generic views 
    '''
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
