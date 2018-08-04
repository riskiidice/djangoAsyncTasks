import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from mimesis import Person

from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    person = Person('en')
    for i in range(total):
        username = 'user_{}'.format(person.full_name())
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)
