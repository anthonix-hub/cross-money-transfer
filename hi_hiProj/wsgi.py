import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hi_hiProj.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
