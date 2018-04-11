from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy('Aashish', 'Mr.', 22, 4.1)


# chat class
class ChatMessage:
    def __init__(self, name, message, isityou):
        self.name = name
        self.message = message
        self.time = datetime.now()
        self.isityou = isityou
