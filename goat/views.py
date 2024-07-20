from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from base.models.goats import Goat

from .forms import GoatForm


class GoatListView(LoginRequiredMixin, ListView):
    model = Goat
    template_name = 'goat/list.html'
    context_object_name = 'goats'


class GoatDetailView(LoginRequiredMixin, DetailView):
    model = Goat
    template_name = 'goat/detail.html'
    context_object_name = 'goat'


class GoatCreateView(LoginRequiredMixin, CreateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class GoatUpdateView(LoginRequiredMixin, UpdateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.manager = self.request.user
        return super().form_valid(form)


class GoatDeleteView(LoginRequiredMixin, DeleteView):
    model = Goat
    template_name = 'goat/confirm_delete.html'
    success_url = reverse_lazy('goat_list')
