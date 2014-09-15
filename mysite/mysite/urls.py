from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from product import views as product_views
from mysite import views

#from django.views.generic.base import TemplateView, SignUpView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^talks/', include('talks.urls', namespace='talks')),
	#url(r'^accounts/login/$',  login),
	#url(r'^accounts/logout/$', logout),
	url(r'^accounts/profile/$', product_views.profile),
	url(r'^signup/$', views.SignUpView.as_view(template_name="signup.html")),
	url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
	#url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^accounts/logout/$', views.LogOutView.as_view(), name='logout'),

)
