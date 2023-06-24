from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Doctor, Comment
from .forms import CommentForm


class DoctorListView(generic.ListView):
    queryset = Doctor.objects.filter(active=True)
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        doctor_id = int(self.kwargs['doctor_id'])
        doctor = get_object_or_404(Doctor, id=doctor_id)
        obj.doctor = doctor
        return super().form_valid(form)
