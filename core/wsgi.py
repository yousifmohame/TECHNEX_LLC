import os

from django.core.wsgi import get_wsgi_application

settings_module = 'core.deployment' if 'WEBSITEHOSTNAME' in os.environ else 'core.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
