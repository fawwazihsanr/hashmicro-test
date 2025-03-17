# engine/urls.py
from django.urls import path

from .views import ModuleView

urlpatterns = [
    path('module', ModuleView.as_view(), name='module_list'),
]