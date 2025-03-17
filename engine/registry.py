import pdb

from django.urls import path, include


class ModuleRegistry:
    def __init__(self):
        self.modules = {}

    def register(self, name, urlconf):
        self.modules[name] = urlconf

    def unregister(self, name):
        if name in self.modules:
            del self.modules[name]

    def get_urlpatterns(self):
        urlpatterns = []
        for name, urlconf in self.modules.items():
            urlpatterns.append(
                path(f'{name}', include(f'{name}.urls'))
            )
        return urlpatterns


registry = ModuleRegistry()