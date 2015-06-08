from django.views.generic import View
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from hospital.models import HospitalDirection, Comment
from forms import CommentForm

# Create your views here.


class HomeView(View):

    def get(self, request):
        return render_to_response('index.html', locals())


class HopitalListView(ListView):

    model = HospitalDirection

    def get_context_data(self, **kwargs):
        context = super(HopitalListView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

   # all_models_dict = {
   #      "template_name": "contacts/index.html",
   #      "queryset": Individual.objects.all(),
   #      "extra_context" : {"role_list" : Role.objects.all(),
   #                         "venue_list": Venue.objects.all(),
   #                         #and so on for all the desired models...
   #                         }
   #  }


def view_hospital(request, slug):
    print slug
    hospital = get_object_or_404(HospitalDirection, slug=slug)
    comments = hospital.hospital_comment.all()
    # print comments
    print "Hospital Slug is {}".format(hospital.slug)
    print hospital
    form = CommentForm(request.POST or None)
    print form
    if form.is_valid():
        print "Fuck Shit"
        comment = form.save(commit=False)
        comment.hospital = hospital
        comment.save()
        # return redirect(request.path)
    return HttpResponseRedirect(reverse('hospital-list'))
