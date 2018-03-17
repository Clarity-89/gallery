from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import User
from .forms import UserProfileForm


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:detail', kwargs={'pk': self.kwargs['pk']})
