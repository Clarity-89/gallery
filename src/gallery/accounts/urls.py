from django.urls import path

from .views import UserProfileDetailView, UserProfileUpdateView

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', UserProfileDetailView.as_view(), name="detail"),
    path('<int:pk>/edit/', UserProfileUpdateView.as_view(), name="edit")
]
