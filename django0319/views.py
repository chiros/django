from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, RegForm
from django.shortcuts import redirect, render


def logout(request):
    logout(reverse_lazy('index'))

class RegView(FormView):
    template_name = 'register2.html'
    form_class = RegForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return redirect('index')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)
