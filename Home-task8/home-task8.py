import json
import datetime

GOLD = 'gold'
SILVER =  'Silver'

class Player(object):

    def __init__(self, email, password, name):
        self.email = str(email)
        self.password = str(password)
        self.name = str(name)
        self.session = []
        self.wallet = {}
        self.counter = {}

    def init_money(self, ):
        money_gold = Money(GOLD, 100)
        money_silver = Money(SILVER, 100)
        print money_gold
        self.wallet = {1: money_gold, 2: money_silver}
        print self.wallet

    def __str__(self):
        format_str = 'email= "{}", password= "{}", name= "{}", wallet= "{}"'
        return format_str.format( self.email, self.password, self.name, self.wallet)

class Session(object):
    def __init__(self, id=None, start_time=None, finish_time=None):
        self.id = int(id)
        self.start_time = datetime.datetime.now()
        self.finish_time = datetime.datetime.now()

class Money(object):
    def __init__(self, name_of_money, counter):
        self.name_of_money = (name_of_money)
        self.counter = counter
    def __str__(self):
        return self.name_of_money, self.counter



if __name__ == "__main__":
    player = Player('mail.@tut.by', '12WW34e', 'drednout')
    money = Money('gold', 100)
    print money, player