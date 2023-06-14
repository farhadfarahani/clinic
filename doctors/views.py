from django.shortcuts import render
from django.views import generic

from .models import Doctor


class DoctorListView(generic.ListView):
    queryset = Doctor.objects.filter(active=True)
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'
