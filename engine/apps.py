from django.apps import AppConfig
from django.db.models.signals import post_migrate


class EngineConfig(AppConfig):
    name = 'engine'

    def ready(self):
        post_migrate.connect(self.create_initial_modules, sender=self)

    def create_initial_modules(self, **kwargs):
        try:
            from .models import InstalledModule
            # Create default modules if needed
            if not InstalledModule.objects.exists():
                InstalledModule.objects.create(name='product', is_active=True)
        except:
            pass