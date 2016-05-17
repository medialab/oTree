from django.core.management.base import BaseCommand
from django.core.cache import cache

def clear():
    cache.clear()

def float_as_percentage(a):
        return int(a * 100)
