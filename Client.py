# new class Client
class Client:
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.money = 0

    # input money
    def add_money(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('Wrong type of money')
        if value < 0:
            raise TypeError('Do you want to add value lower than 0?')
        self.money += value

    # withdrawal money
    def remove_money(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('Wrong type of money')
        if self.money < value:
            raise TypeError('You do not have enought money')
        self.money -= value

    # show details for one client
    def cash(self):
        if self.money == 0:
            print("Don't have money")
        else:
            print('{} {} has {}$'.format(self.name, self.username, self.money))

