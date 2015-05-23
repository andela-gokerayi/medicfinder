from django.views.generic import View
from django.shortcuts import render, render_to_response
from django.views.generic.list import ListView 
from hospital.models import *
from endless_pagination.decorators import page_template

# Create your views here.
class HomeView(View):
    
    def get(self, request):
        return render_to_response('index.html', locals())

class HopitalListView(ListView):

    model = HospitalDirection
    def get_context_data(self, **kwargs):
        context = super(HopitalListView, self).get_context_data(**kwargs)
        return context