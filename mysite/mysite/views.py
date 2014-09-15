#from __future__ import absolute_import


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product
from talks.models import TalkList
import json


from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.views import generic
from braces import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#function based views way
#@login_required
#def logout_view(request):
#messages.success(request, 'message here')
#return HttpResponseRedirect

# Create your views here.
def home(request):
	products = Product.objects.order_by('-price')[:5]
	return render(request, 'home.html', {'products': products})

class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.CreateView):
	form_class = RegistrationForm
	form_valid_message = 'Thanks for signing up. You can now login'
	model = User
	success_url = reverse_lazy('home')
	template_name = 'signup.html'
	def form_valid(self, form):
		 resp = super(SignUpView, self).form_valid(form)
		 TalkList.objects.create(user=self.object, name='To Attend')
		 return resp




class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.FormView):
    form_class = LoginForm
    form_valid_message = 'You are now logged in '
    success_url = reverse_lazy('home')
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)