from django.views.generic import DetailView, ListView

from .models import Photo


class PhotoListView(ListView):
    queryset = Photo.objects.all()
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    queryset = Photo.objects.all()
    context_object_name = 'photo'
