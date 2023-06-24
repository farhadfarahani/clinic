from django.urls import path

from .views import DoctorListView, DoctorDetailView, CommentCreateView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('comment/<int:doctor_id>/', CommentCreateView.as_view(), name='comment_create'),
]
