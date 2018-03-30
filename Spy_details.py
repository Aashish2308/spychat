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


friend_one = Spy('Praveen', 'Mr.', 19, 4.7)
friend_two = Spy('Ajit', 'Mr.', 23, 4.8)
friend_three = Spy('Kamini', 'Dr.', 24, 4.8)
friend_four = Spy('Ritesh', 'Mr..', 22, 4.9)
friend_five = Spy('Harshika', 'Ms.', 25, 4.9)
friend_six = Spy('Krishna', 'Dr.', 24, 4.9)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]