from abc import ABC, abstractmethod

import Messages as msgs


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message: msgs):
        pass

class SmsSender(MessageSender):

    def send_message(self, message: msgs):
        if isinstance(message, msgs.TextMessage):
            print("SMS: Отправляю текстовое сообщение через СМС...")
            return True
        else:
            print("SMS: Я умею отправлять только текстовое сообщение!")
            return False


class TelegramSender(MessageSender):

    def send_message(self, message: msgs):
        print(f"TELEGRAM: Отправляю сообщение в телеграм, получатель: {message.recipient}..")
        return True

class VkSender(MessageSender):

    def send_message(self, message: msgs):
        print(f"VK: Отправляю сообщение во вконтакте, получатель: {message.recipient}..")
        return True