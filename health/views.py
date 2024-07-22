from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from base.models.healths import Health
from base.views import custom_error_view

from .forms import HealthForm


class HealthListView(LoginRequiredMixin, ListView):
    model = Health
    template_name = 'health/list.html'
    context_object_name = 'health_records'

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


class HealthDetailView(LoginRequiredMixin, DetailView):
    model = Health
    template_name = 'health/detail.html'
    context_object_name = 'health'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class HealthCreateView(LoginRequiredMixin, CreateView):
    model = Health
    form_class = HealthForm
    template_name = 'health/form.html'
    success_url = reverse_lazy('health_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = 'admin' if self.request.user.is_superuser else self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return custom_error_view(request, exception=e)


class HealthUpdateView(LoginRequiredMixin, UpdateView):
    model = Health
    form_class = HealthForm
    template_name = 'health/form.html'
    success_url = reverse_lazy('health_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.manager = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class HealthDeleteView(LoginRequiredMixin, DeleteView):
    model = Health
    template_name = 'health/confirm_delete.html'
    success_url = reverse_lazy('health_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except PermissionDenied:
            return HttpResponseRedirect(reverse_lazy('health_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)
