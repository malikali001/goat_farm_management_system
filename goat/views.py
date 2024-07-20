from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from base.models.goats import Goat

from .forms import GoatForm


class GoatListView(ListView):
    model = Goat
    template_name = 'goat/list.html'
    context_object_name = 'goats'


class GoatDetailView(DetailView):
    model = Goat
    template_name = 'goat/detail.html'
    context_object_name = 'goat'


class GoatCreateView(CreateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class GoatUpdateView(UpdateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')


class GoatDeleteView(DeleteView):
    model = Goat
    template_name = 'goat/confirm_delete.html'
    success_url = reverse_lazy('goat_list')
