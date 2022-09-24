import vk_api

login_timur = '79876164600'
password_timur = 'electramightygrace23'

# login_alina = '79373450512'
# password_alina = 'vikkibye'


def edit_status_vk(login, password):
    vkapi = vk_api.VkApi(login=login, password=password)
    vkapi.auth()

    status = vkapi.method('status.get')
    status_part = status['text'].split(' ')
    status_part[4] = str(int(status_part[4]) + 1)
    status = ' '.join(status_part)
    status = vkapi.method('status.set', values={'text': status})


edit_status_vk(login_timur, password_timur)
# edit_status_vk(login_alina, password_alina)
