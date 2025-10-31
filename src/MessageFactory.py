import enum

from src.MessageSender import MessageSender
from src.Messages import TextMessage, ImageMessage, VideoMessage, FileMessage


class MessageType(enum.Enum):
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    FILE = 4

class MessageFactory:

    @staticmethod
    def create_message(type, content, sender, recipient, msg_sender: MessageSender):
        match type:
            case MessageType.TEXT:
                return TextMessage(content, sender, recipient, msg_sender)
            case MessageType.IMAGE:
                return ImageMessage(content, sender, recipient, msg_sender)
            case MessageType.VIDEO:
                return VideoMessage(content, sender, recipient, msg_sender)
            case MessageType.FILE:
                return FileMessage(content, sender, recipient, msg_sender)
