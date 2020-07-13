import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    random_id = random.getrandbits(64)  # 64 бита
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':random_id})


# API-ключ созданный ранее
token = "3dd31c959632a99c0c3b01be18bed4446347ed345e77a865f3dd0b46b0a7ede25228cd75f2ba06ec6e5d4"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")