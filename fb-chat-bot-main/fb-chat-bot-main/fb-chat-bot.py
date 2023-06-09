from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import openai
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]
            print(msg)

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );

                """.format(str(author_id).replace('"', '""')))

                c.execute("""

                INSERT INTO "{}" VALUES (?, ?)

                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass

elif ("Open book" in msg or "open" in msg):
    reply = "me top"
    sendMsg()
elif (msg == "Open book!"):
    reply = "me top"
    sendMsg()



cookies = {
    "sb": "9YJzZHEdvKdk95WBtmx0T1PL",
    "fr": "0GF1LAy4bWPHKKgCs.AWWNl_VXDJ1sVCTwdDKrtSMSNt4.Bkc4MQ.ef.AAA.0.0.Bkc4MQ.AWVaWv4bHR8",
    "c_user": "100040501305417",
    "datr": "7oJzZCTGK-6-T9auuEqENNSi",
    "xs": "12%3AEiye9wK0bX-_iQ%3A2%3A1685291791%3A-1%3A7247"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
