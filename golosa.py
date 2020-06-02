import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
x=123456

def lol(user_id,message):
	vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':x})
	
token='c2e514f79dd6d1930905f9f32d103b20b6a177fc8906662818468804aaf2e528f69cf23528bce29fc80d5'
vk=vk_api.VkApi(token=token)
longpoll=VkLongPoll(vk)
print('бот работает : )')
for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW:
                x+=1
                if event.to_me:
                        r=event.text
                        print(event.user_id,r)
                        if r=='Голоса' or r=='голоса':#если сообщение для бота голоса то
                                lol(event.user_id,'тут текст и ссылка')
                                #иначе отправить это
                        else:
                                lol(event.user_id,'Пшель в жепу')
