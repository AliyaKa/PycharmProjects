
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from config.users.views import CustomUserViewSet
from .models import CustomUser as User


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'Пушкин', 'email': 'a@mail.ru'}, format='json')
        view = CustomUserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/user/', {'username': 'Пушкин', 'email': 'a@mail.ru'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = CustomUserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(username='Пушкин', email='a@mail.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(username='Пушкин', email='a@mail.ru')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'username': 'Грин', 'email': 'g@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(username='Пушкин', email='a@gmail.com')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', '1')
        client.force_authenticate(user=admin)
        response = client.put(f'/api/users/{user.id}/', {'username': 'Грин', 'email': 'g@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'Грин')
        self.assertEqual(user.email, 'g@mail.ru')
        client.logout()


class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_admin(self):
    #     user = User.objects.create(username='Пушкин', email='a@gmail.co')
    #     project = Projects.objects.create(title='Пиковая дама', users=[user])
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com', '1')
    #     self.client.login(username='admin', password='1')
    #     self.project.save()
    #     response = self.client.put(f'/api/projects/{project.id}/', {'title': 'Руслан и Людмила',
    #                                                                 'users': project.user.id})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    # def test_edit_mixer(self):
    #     project = mixer.blend(Projects)
    #     admin = User.objects.create_superuser('admin', 'admin@admin.com','admin123456')
    #     self.client.login(username='admin', password='admin123456')
    #     response = self.client.put(f'/api/projects/{project.id}/',
    #                                {'title': 'Руслан и Людмила', 'users': project.users})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Projects.objects.get(id=project.id)
    #     self.assertEqual(project.title, 'Руслан и Людмила')
