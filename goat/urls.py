from django.urls import path

from .views import (GoatCreateView, GoatDeleteView, GoatDetailView,
                    GoatListView, GoatUpdateView)

urlpatterns = [
    path('', GoatListView.as_view(), name='goat_list'),
    path('<int:pk>/', GoatDetailView.as_view(), name='goat_detail'),
    path('add/', GoatCreateView.as_view(), name='goat_create'),
    path('<int:pk>/edit/', GoatUpdateView.as_view(), name='goat_update'),
    path('<int:pk>/delete/', GoatDeleteView.as_view(), name='goat_delete'),
]
