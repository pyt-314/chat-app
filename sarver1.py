# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:52:37 2022

@author: luigi
"""

import socket
import sqlite3
import pickle
# server.py
listup = []
ip_address = '127.0.0.1'
ip ='220.254.0.171'
port = 7010
buffer_size = 8192
con = sqlite3.connect('chat.db')
cur = con.cursor()

# Socketの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IP Adress とPort番号をソケット割り当てる
    s.bind((ip_address, port))
    print("f")
    # Socketの待機状態
    s.listen(3)
    # while Trueでクライアントからの要求を待つ
    while True:
        # 要求があれば接続の確立とアドレス、アドレスを代入
        con = sqlite3.connect('chat.db')
        cur = con.cursor()
        conn, addr = s.accept()
        # データを受信する
        data = conn.recv(buffer_size)
        print(data)
        data = pickle.loads(data)
        if data[0] == "load":
            listup = []
            for user,texts in cur:
                listup += [(user,texts)]
        if data[0] == "add":
            cur.execute("INSERT INTO texts VALUES (?, ?)",data[1:])
            listup = []
            for user,texts in cur:
                listup += [(user,texts)]
        print(listup)
        listup = pickle.dumps(listup)
        con.commit()
        con.close()
        #print('data-> {}, addr->{}'.format(data, addr))
        # データを送信する
        conn.sendall(listup)
        #conn.close()