from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from usuario_app.forms import SignUpForm


class RegistroUsuarioView(CreateView):
    
    model = User  # Assuming you're using the built-in User model
    form_class = SignUpForm
    template_name = 'usuario_app/signup.html'
    success_url = 'login/'  # Redirect to login page after successful signup
    
  
    def form_valid(self, form):
        if self.request.method == 'POST':
            user = form.save()
        # ...

        return super().form_valid(form)  # Call the default form saving behavior

