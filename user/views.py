from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from base.models.custom_users import CustomUser
from base.views import custom_error_view

from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'
    next_page = reverse_lazy('login')


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/list.html'
    context_object_name = 'users'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return custom_error_view(request, exception=e)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user/detail.html'
    context_object_name = 'user'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('user_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/add.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return custom_error_view(request, exception=e)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('user_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'user/confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('user_list'))
        except Exception as e:
            return custom_error_view(request, exception=e)
