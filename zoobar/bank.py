from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    bankdb = bank_setup()
    senderb = bankdb.query(Bank).get(sender)
    recipientb = bankdb.query(Bank).get(recipient)

    sender_balance = senderb.zoobars - zoobars
    recipient_balance = recipientb.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderb.zoobars = sender_balance
    recipientb.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    if bank is None:
        bank = Bank()
        bank.username = username
        bank.zoobars = 10
    return bank.zoobars
 
def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

