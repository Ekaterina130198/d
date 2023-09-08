# Екатерина Прудникова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data


# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,

                         json=body,

                         headers=data.headers)


response = post_new_order(data.user_body);

response = get_auth_track(data.user_body)

print(response.status_code)

# Сохранение трека заказа
get_auth_track():

order_response = my_diplom_progect.post_new_order(data.order_body)

auth_track = order_response.json()["authtrack"]

return auth_track

# Получение заказа по треку
def get_order_track(order_track):

return requests.post(configuration.my_diplom_progect + configuration.ORDERS_GET(data.order_track))

response = get_order_track(data.order_track);

print(response.status_code)

assert response.status_code == 201

assert kit_response.json()["authtrack"] != ""

response = get_order_track(auth_track)