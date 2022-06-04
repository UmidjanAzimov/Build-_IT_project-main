from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AddUserCreationForm

# Create your views here.

class AddUserSignUp(CreateView):
    form_class = AddUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'mutaxasissignup.html'

    
class AddUserSignUp1(CreateView):
    form_class = AddUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'firmasignup.html'


class AddUserSignUp2(CreateView):
    form_class = AddUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'buyurtmachisignup.html'


