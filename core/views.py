from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from core.utils import openkra

password = 'mEt@sploit10i'


@csrf_exempt
def main(request):
    if request.method == 'POST':
        try:
            kra_pin = request.POST.get('pin')
            openkra(pin=kra_pin, password=password)
        except Exception as e:
            print(e)
    return HttpResponse('Job completed')


