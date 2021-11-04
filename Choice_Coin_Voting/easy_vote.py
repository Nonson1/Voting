# Copyright Fortior Blockchain, LLLP 2021
# Apache License
# This is a work in progress to create a simplified backend voting architecture.
# This software is under construction.

# Imports
from algosdk import account, encoding, mnemonic,transaction
from algosdk.future.transaction import AssetTransferTxn, PaymentTxn
from algosdk.v2client import algod

from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import write_to_file
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn
from algosdk.future.transaction import AssetTransferTxn

# Put Algod Client address here
algod_address = "https://testnet-algorand.api.purestake.io/idx2" 
# Put Algod Token here
algod_token = "" 
headers = {"X-API-Key": algod_token }
# Initializes client for node.
algod_client = algod.AlgodClient(algod_token,algod_address,headers)
# Choice Asset ID.
asset = 42771692 

# VOID TEST ADDRESS
address = "VSHR4VD3KO362VZJS3TGL7IM4Z6MYEWHXV6TUQPVCRLADRNRKQ63JHJRTM"
# Create new address from scratch
# Variational where each option has an address
# VOID TEST ADDRESS
voter_address = ""
voter_phrase = ""

def vote():
    voter = input(str("Vote 0 for zero and vote 1 for one:"))
    params = algod_client.suggested_params()
    if voter is str('1'):
        # send one choice to address
        txn = AssetTransferTxn(sender=voter_address, sp=params, receiver=address, amt=1, index=asset)
        print ("Thanks for voting for one.")
    else:
        # send zero choice to address
        print ("Thanks for voting for zero.")
vote()
    #def make_vote(sender, key, receiver, amount, comment):
        #"""This function is the same as the one found in `vote.py`"""
        #parameters = algod_client.suggested_params()
        #transaction = AssetTransferTxn(sender, parameters, receiver, amount, asset, note=comment)

        #signature = transaction.sign(key)
        #algod_client.send_transaction(signature)
        #final = transaction.get_txid()
        #return True, final

def calculate():
    # Check total Choice in Address
    account_info = algod_client.account_info(address)
    assets = account_info.get("assets") 
    amount = asset.get("amount")
    option_zero = amount * 1
    total_vote = input("Total votes:", total_vote)
    option_one = total_vote - option_one
    print("Option zero:", option_zero) 
    print("Option one:", option_one)
#calculate()

    #def get_balance(address):
        #"""Get the balance of a wallet."""
        #account = algod_client.account_info(address)
        #return account["amount"]

def winner():
    if option_zero > option_one:
        print("Option zero wins.")
    else:
        print("Option one wins.")
#winner()
