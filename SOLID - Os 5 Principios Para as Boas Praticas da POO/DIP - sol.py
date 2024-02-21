from abc import ABC, abstractmethod

class INotifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(INotifier):
    def send(self, message):
        print(f"Enviando e-mail: {message}")

class SMSNotifier(INotifier):
    def send(self, message):
        print(f"Enviando SMS: {message}")

class NotificationManager:
    def __init__(self, notifiers: list[INotifier]):
        self.notifiers = notifiers

    def sendNotification(self, message):
        for notifier in self.notifiers:
            notifier.send(message)
