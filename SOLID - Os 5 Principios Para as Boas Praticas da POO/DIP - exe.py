# Para aprofundar a atividade sobre o Princípio da Inversão de Dependência (DIP), 
# consideraremos um sistema de notificações para uma aplicação. Este sistema permite enviar notificações por diferentes meios, 
# como e-mail, SMS e notificações push. A implementação inicial viola o DIP, pois os componentes de alto nível dependem diretamente de 
# implementações específicas de baixo nível, em vez de abstrações.

class EmailNotifier:
    def send(self, message):
        print(f"Enviando e-mail: {message}")

class SMSNotifier:
    def send(self, message):
        print(f"Enviando SMS: {message}")

class NotificationManager:
    def __init__(self):
        self.email_notifier = EmailNotifier()
        self.sms_notifier = SMSNotifier()

    def sendNotification(self, message, type):
        if type == "email":
            self.email_notifier.send(message)
        elif type == "sms":
            self.sms_notifier.send(message)
