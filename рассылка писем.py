def send_email(message, recipient, sender='university.help@gmail.com'):


    if '@' not in recipient or not recipient.endswith('.com', '.ru', '.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} ')
        return
    if recipient == sender:
        print("Невозможно отправить письмо самому себе")
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПАРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return


send_email('dthth', 'vasyok1337@gmail.com', 'university.help@gmail.com')
