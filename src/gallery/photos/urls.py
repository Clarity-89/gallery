from django.urls import path
from .views import PhotoDetailView, PhotoListView

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
    path('photos/<int:id>', PhotoDetailView.as_view(), name='detail')
]
