import os
import django

# Run this to clear all sessions for data base or when kept the site open for long time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
django.setup()

from django.contrib.sessions.models import Session


Session.objects.all().delete()
print("All sessions cleared successfully!")
