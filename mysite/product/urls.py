from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<search>[a-z]+)/$', views.search, name='search'),

    url(r'^sort/(?P<sort>.+)/$', views.sort_products, name='sort'),

    url(r'^sortprofile/(?P<sort>[a-z]+)/$', views.sort_products_profile, name='sort_profile'),

    # ex: /polls/5/results/
    #url(r'^(?P<id>[0-9]+)/results/$', views.results, name='vodka'),
    # ex: /polls/5/vote/
    #url(r'^(?P<id>[0-9]+)/vote/$', views.vote, name='vote'),   



]