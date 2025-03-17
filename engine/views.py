import pdb
from importlib import reload, import_module

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import clear_url_caches
from django.views import View

from .models import InstalledModule
from .registry import registry


class ModuleView(View):
    def get(self, request):
        modules = InstalledModule.objects.all()

        for module in modules.filter(is_active=True):
            registry.register(module.name, module.base_url)

        reload_urlconf()
        module_urls = {
            module.name: module.base_url for module in modules if module.is_active
        }
        return render(request, 'module.html', {'modules': modules, 'module_urls': module_urls})

    def post(self, request):
        module_name = request.POST.get('module_name')
        if not module_name:
            return JsonResponse({'error': 'Module name is required'}, status=400)

        base_url = f"/{module_name}"
        module = InstalledModule.objects.filter(name=module_name, is_active=False).last()

        if module:
            module.base_url = base_url
            module.is_active = True
            module.save()
            registry.register(module_name, base_url)
            reload_urlconf()

        return redirect('module_list')

    def delete(self, request):
        module_name = request.GET.get('module_name')
        if not module_name:
            return JsonResponse({'error': 'Module name is required'}, status=400)

        module = InstalledModule.objects.filter(
            name=module_name,
            is_active=True
        ).last()

        if module:
            module.is_active = False
            module.save()
            registry.unregister(module_name)
            reload_urlconf()
        return redirect('module_list')


def reload_urlconf():
    clear_url_caches()
    reload(import_module(settings.ROOT_URLCONF))