from django.urls import path

from .views import (HealthCreateView, HealthDeleteView, HealthDetailView,
                    HealthListView, HealthUpdateView)

urlpatterns = [
    path('', HealthListView.as_view(), name='health_list'),
    path('<int:pk>/', HealthDetailView.as_view(), name='health_detail'),
    path('create/', HealthCreateView.as_view(), name='health_create'),
    path('<int:pk>/update/', HealthUpdateView.as_view(), name='health_update'),
    path('<int:pk>/delete/', HealthDeleteView.as_view(), name='health_delete'),
]
