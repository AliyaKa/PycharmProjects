from mixer.backend.django import mixer
from django.core.management.base import BaseCommand
from config.todo.models import Projects, ToDo


class Command(BaseCommand):
    help = 'Create project and todo'

    def handle(self, *args, **options):
        for i in range(5):
            mixer.blend(Projects)
            mixer.blend(ToDo)
        print('done')
