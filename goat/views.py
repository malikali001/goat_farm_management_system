from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from base.models.goats import Goat
from base.views import custom_error_view

from .forms import GoatForm


class GoatListView(LoginRequiredMixin, ListView):
    model = Goat
    template_name = 'goat/list.html'
    context_object_name = 'goats'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(manager=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return custom_error_view(request, exception=e)


class GoatDetailView(LoginRequiredMixin, DetailView):
    model = Goat
    template_name = 'goat/detail.html'
    context_object_name = 'goat'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class GoatCreateView(LoginRequiredMixin, CreateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return custom_error_view(request, exception=e)


class GoatUpdateView(LoginRequiredMixin, UpdateView):
    model = Goat
    form_class = GoatForm
    template_name = 'goat/form.html'
    success_url = reverse_lazy('goat_list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.manager = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class GoatDeleteView(LoginRequiredMixin, DeleteView):
    model = Goat
    template_name = 'goat/confirm_delete.html'
    success_url = reverse_lazy('goat_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('goat_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)
