#module_3_2 Способы вызова функции

def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    recipient_flag = False
    sender_flag = False

    # просто чтобы разгрузить код дальше
    len_rec = len(recipient)-4
    len_sen = len(sender)-4

    #проверка адресата
    if recipient.find('@') ==-1:
        recipient_flag = False
    elif recipient.find('.net') == len_rec or recipient.find('.com') == len_rec or recipient.find('.ru') == (len_rec+1):
        recipient_flag = True

    #проверка отправителя
    if sender.find('@') ==-1:
        sender_flag = False
    elif  sender.find('.net') == len_sen or sender.find('.com') == len_sen or sender.find('.ru') == (len_sen+1):
        sender_flag = True

    #выбор события от наименее вероятного
    if recipient_flag == False or sender_flag == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}','\n')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!','\n')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}','\n')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}','\n')


#Тестовые сообщения из урока
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

#Ещё тестовые сообщения
send_email('Test', 'blabla.ru.net.com', sender = 'bla@.net.com.ru')     #нет @
send_email('Test', 'bla@.ru.net.com', sender = 'bla@.net.com.ru')       #должно ли работать?
send_email('Test', 'blabla@.ru.net.com.uk', sender = 'bla@.net.com.ru') #не заканчивается на подходящий домен
send_email('Test', 'blabla@.ru.net.uk.com') #все хорошо