from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context
