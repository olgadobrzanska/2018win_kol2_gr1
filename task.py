from Bank import *
from Client import *

bank = Bank("moj_bank")
bank2 = Bank("moj_bank2")
client1 = Client("Andrzej", "Kowalski")
client2 = Client("Anna", "Nowak")
client3 = Client("Grzegorz", "Aaaa")
client4 = Client("Katarzyna", "Bbbb")

bank.add_client(client1)
bank.add_client(client2)

bank2.add_client(client3)
bank2.add_client(client4)

client1.add_money(200)
client1.remove_money(50)
client1.add_money(2)
client2.add_money(1200)
client3.add_money(15000)
client4.add_money(160)
print('Show client - bank')
bank.show_all_clients()
print('\nShow client - bank2')
bank2.show_all_clients()

print('\nShow money')
client1.cash()
client2.cash()
print('\nAfter transfer')
bank.transfer_money(client1, client2, 20)
client1.cash()
client2.cash()

print('\nShow money')
client1.cash()
client3.cash()
print('\nAfter transfer')
bank.transfer_money(client1, client3, 100)
client1.cash()
client3.cash()