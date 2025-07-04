from datetime import timedelta
from django.utils import timezone

def generate_expire_time(hours: int):
    return timezone.now() + timedelta(hours=hours)