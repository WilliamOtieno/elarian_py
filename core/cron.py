import time

from .models import TaxQueue
from .utils import openkra
from .views import password


def file_returns():
    tasks = TaxQueue.objects.filter(filed=False)
    for task in tasks:
        openkra(pin=task.kra_pin, password=password)
        print('Checked for KRA Status...')
        time.sleep(2)
