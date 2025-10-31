from src.MessageFactory import MessageFactory, MessageType
from src.MessageSender import SmsSender, TelegramSender, VkSender


def app():
    sms_sender = SmsSender()
    tg_sender = TelegramSender()
    vk_sender = VkSender()

    text_msg = MessageFactory.create_message(MessageType.TEXT, "Всем привет", "Danil", "FEFU", tg_sender)
    image_msg = MessageFactory.create_message(MessageType.TEXT, "ФОТО", "Danil", "Avito", sms_sender)
    video_msg = MessageFactory.create_message(MessageType.TEXT, "ЧВИДКО", "Danil", "ПрогинЧат", vk_sender)
    file_msg = MessageFactory.create_message(MessageType.TEXT, "Типо файл", "Danil", "GoogleDrive", tg_sender)

    text_msg.send()
    image_msg.send()
    video_msg.send()
    file_msg.send()

if __name__=="__main__":
    app()