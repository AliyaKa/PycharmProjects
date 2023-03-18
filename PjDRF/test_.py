# import requests
# import time
#
# DOMAIN = 'http://127.0.0.1:8000'
#
#
# def timeout():
#     time.sleep(2)
#
#
# def get_url(url):
#     return f'{DOMAIN}{url}'
#
#
# timeout()
# # не авторизован
# response = requests.get(get_url('/api/users/'))
# assert response.status_code == 200
#
# timeout()
# # базовая авторизация
# response = requests.get(get_url('/api/users/'), auth=('admin', '1'))
# assert response.status_code == 200
#
# timeout()
# # авторизация по токену
# TOKEN = requests.post(get_url('/api-token/'), data={'username': 'admin', 'password': '1'}).json().get('token')
# headers = {'Authorization': f'Token {TOKEN}'}
# response = requests.get(get_url('/api/users/'), headers=headers)
# assert response.status_code == 200
#
# timeout()
#
#
# # авторизация по jwt
# # получаем токен
# response = requests.post(get_url('/api/token'), data={'username': 'admin', 'password': '1'})
# result = response.json()
# # наш токен
# access = result['access']
# print('Первый токен', access, end=f'\n{150*"*"}\n')
# # рефреш
# refresh = result['refresh']
# print('refresh', refresh, end=f'\n{150*"*"}\n')
# timeout()
# # авторизуемся с токеном
# headers = {'Authorization': f'Bearer {access}'}
# response = requests.get(get_url('/api/users/'), headers=headers)
# assert response.status_code == 200
# timeout()
# # Обновляем
# response = requests.post(get_url('/api/token/refresh/'), data={'refresh': refresh})
# result = response.json()
# access = result['access']
# print('Обновленный токен', access, end=f'\n{150*"*"}\n')
# print('refresh', refresh, end=f'\n{150*"*"}\n')
#
#
#
