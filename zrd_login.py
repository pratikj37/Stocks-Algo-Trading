from kiteconnect import KiteConnect, KiteTicker
import pdb
import kiteconnect
import pandas as pd
import datetime
import os

api_key = "insert_key_here"                  #api_key
api_secret = "inser_secret_key_here"         #secret_key
filename = str(datetime.datetime.now().date()) + 'token' + '.txt'

def read_access_token_from_file():
    file = open(filename, 'r+')
    access_token = file.read()
    file.close()
    return access_token

def send_access_token_to_file(access_token):
    file = open(filename, 'w')
    file.write(access_token)
    file.close()


def get_login(api_key, api_secret):
    global kwa, kite
    kite = KiteConnect(api_key=api_key)
    print("Logging into Zerodha")

    if filename not in os.listdir():

        print("[*] Generate Request Token : ", kite.login_url())
        request_tkn = input("[*] Enter Your Request Token Here: ")
        data = kite.generate_session(request_tkn, api_secret=api_secret)
        access_token = data["access_token"]
        kite.set_access_token(access_token)
        kws = KiteTicker(api_key, access_token)
        send_access_token_to_file(access_token)

    elif filename in os.listdir():
        print("Already Logged In for Today")
        access_token = read_access_token_from_file()
        kite.set_access_token(access_token)
        kws = KiteTicker(api_key, access_token)

    return kite

kite = get_login(api_key, api_secret)


