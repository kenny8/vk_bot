import vk_api
import random
from vk_bot import VkBot
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

print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)