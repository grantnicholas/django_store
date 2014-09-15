from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from braces import views
from . import models
from . import forms

class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TalkListDetailView(
    RestrictToUserMixin,
    #views.PrefetchRelatedMixin,
    generic.DetailView
):
    model = models.TalkList
    prefetch_related = ('talks',)



class TalkListListView(
	RestrictToUserMixin,
	generic.ListView,
):
    model = models.TalkList


class TalkListCreateView(
     views.LoginRequiredMixin,
     generic.CreateView
 ):
     form_class = forms.TalkListForm
     model = models.TalkList

     def form_valid(self, form):
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return super(TalkListCreateView, self).form_valid(form)
