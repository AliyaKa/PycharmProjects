from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from config.users.models import CustomUser


class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def handle(self, *args, **options):
        for i in range(5):
            mixer.blend(CustomUser)
        print('done')

