from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context


def custom_error_view(request, exception=None):
    context = {
        'message': 'An unexpected error has occurred. Please try again later.',
    }
    return render(request, 'custom_error.html', context)
