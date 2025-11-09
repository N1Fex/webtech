from src.MessageCreator import TextMessageCreator, ImageMessageCreator, VideoMessageCreator, FileMessageCreator
from src.MessageSender import SmsSender, TelegramSender, VkSender


def app():
    sms_sender = SmsSender()
    tg_sender = TelegramSender()
    vk_sender = VkSender()

    text_msg = TextMessageCreator.create_message("Всем привет", "Danil", "FEFU", tg_sender)
    image_msg = ImageMessageCreator.create_message("ФОТО", "Danil", "Avito", sms_sender)
    video_msg = VideoMessageCreator.create_message("ЧВИДКО", "Danil", "ПрогинЧат", vk_sender)
    file_msg = FileMessageCreator.create_message("Типо файл", "Danil", "GoogleDrive", tg_sender)

    text_msg.send()
    image_msg.send()
    video_msg.send()
    file_msg.send()

if __name__=="__main__":
    app()