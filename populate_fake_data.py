import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newTex.settings')

import django
django.setup()

import random
from faker import Faker

from django.contrib.auth.models import User


fake = Faker()


def populate(n):
    for entry in range(n):
        username = fake.simple_profile().get('username')

        User.objects.get_or_create(username=username, password=username)


if __name__ == '__main__':
    print('Populating data...')
    populate(10)
    print('Populating complete')