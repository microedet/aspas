from django import forms
from .forms import UserCreationEmail
from django.views.generic import CreateView
from django.urls import  reverse_lazy

# Create your views here.
class SigUpView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationEmail

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

    def get_form(self, form_class=None):
        form = super(SigUpView,self).get_form()
        #modifico los campos en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        return form
