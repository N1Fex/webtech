from abc import ABC
import MessageSender

class Message(ABC):

    def __init__(self, content, sender, recipient, msg_sender: MessageSender):
        self.content = content
        self.sender = sender
        self.recipient = recipient
        self.msg_sender = msg_sender

    def send(self):
        return self.msg_sender.send_message(self)

class TextMessage(Message):

    def __init__(self, content, sender, recipient, msg_sender: MessageSender):
        super().__init__(content, sender, recipient, msg_sender)

class ImageMessage(Message):

    def __init__(self, content, sender, recipient, msg_sender: MessageSender):
        super().__init__(content, sender, recipient, msg_sender)

class VideoMessage(Message):

    def __init__(self, content, sender, recipient, msg_sender: MessageSender):
        super().__init__(content, sender, recipient, msg_sender)

class FileMessage(Message):

    def __init__(self, content, sender, recipient, msg_sender: MessageSender):
        super().__init__(content, sender, recipient, msg_sender)