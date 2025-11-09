from abc import ABC

from src.MessageSender import MessageSender
from src.Messages import Message, TextMessage, FileMessage, VideoMessage, ImageMessage


class MessageCreator(ABC):

    @staticmethod
    def create_message(content: str, sender: str, recipient: str, msg_sender: MessageSender) -> Message:
        pass

class TextMessageCreator(ABC):

    @staticmethod
    def create_message(content: str, sender: str, recipient: str, msg_sender: MessageSender) -> Message:
        return TextMessage(content, sender, recipient, msg_sender)

class ImageMessageCreator(ABC):

    @staticmethod
    def create_message(content: str, sender: str, recipient: str, msg_sender: MessageSender) -> Message:
        return ImageMessage(content, sender, recipient, msg_sender)

class VideoMessageCreator(ABC):

    @staticmethod
    def create_message(content: str, sender: str, recipient: str, msg_sender: MessageSender) -> Message:
        return VideoMessage(content, sender, recipient, msg_sender)

class FileMessageCreator(ABC):

    @staticmethod
    def create_message(content: str, sender: str, recipient: str, msg_sender: MessageSender) -> Message:
        return FileMessage(content, sender, recipient, msg_sender)