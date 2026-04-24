import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_pascards = Passcard.objects.filter(is_active=True)
    print('Количество пропусков:', Passcard.objects.count())
    print('Активных пропусков:', len(active_pascards))