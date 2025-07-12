import os
import profile
import sys
from pathlib import Path

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 400

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

django.setup()

from apps.products.models import Product, Price

if __name__ == '__main__':
    print('deucerto')