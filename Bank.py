from Client import Client


# new class Bank
class Bank:
    def __init__(self, name):
        self.name = name
        self.all_clients = []

    # add new client
    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError('Variable is not a Client')
        self.all_clients.append(client)

    # show clients in the bank
    def show_all_clients(self):
        if self.all_clients == 0:
            print('No clients in this bank.')
        else:
            for x in self.all_clients:
                print(x.username, x.name, x.money, '$')

    # transfer money from one client to another
    def transfer_money(self, client1, client2, value):
        if not isinstance(client1, Client) or not isinstance(client2, Client) or not isinstance(value, (float, int)):
            raise TypeError('Argument is wrong')
        try:
            client1.remove_money(value)
            client2.add_money(value)
        except ValueError:
            raise TypeError('Something goes wrong')
