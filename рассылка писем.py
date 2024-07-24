def send_email(message, recipient, sender="university.help@gmail.com"):
    """
    Функция для отправки письма.

    :param message: Сообщение, которое нужно отправить.
    :param recipient: Адрес получателя.
    :param sender: Адрес отправителя (по умолчанию "university.help@gmail.com").
    """
    # Проверка на корректность e-mail
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры использования функции
send_email("Привет, как дела?", "student@example.com")
send_email("Привет, как дела?", "student@example.com", sender="custom.sender@gmail.com")
send_email("Привет, как дела?", "student@example.com", sender="university.help@gmail.com")
send_email("Привет, как дела?", "student@example")  #
send_email("Привет, как дела?", "university.help@gmail.com", sender="university.help@gmail.com")
