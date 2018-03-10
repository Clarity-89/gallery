from django.urls import path
from .views import PhotoDetailView, PhotoListView

app_name = 'photos'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='detail')
]
