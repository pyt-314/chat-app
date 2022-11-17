# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:57:13 2022

@author: luigi
"""

import socket
import bottle
import pickle

html = """
<!DOCTYPE html>
<html lang="ja">
<head>
<mate charset="UTF-8">
<title>爆弾！投下ぁ！</title>
</head>
<body>
{}
</body>
</html>
"""
name = ""
chat = []
show = ""
def p(text):
    ret = ""
    for i in range(len(text)):
        ret += "<p>"+ text[0]+":"+text[1]+"</p>"+"\n\r"
    return ret
@bottle.get('/')
def index():
    global chat
    ip_address = '127.0.0.1'
    port = 7010
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    data = pickle.dumps(["load","",""])
    print(data)
    s.sendall(data)
    chat = pickle.loads(s.recv(8192))
    show = p(chat)
    
    return '''
        <form action = "/" method = "post">
            Username: <input name = "username" type = "text" />
            <input value = "チャットへ!" type = "submit"/>
        </form>
    '''
@bottle.post('/')  
def show():
    global s,chat,name,show
    show = p(chat)
    name = bottle.request.forms.get("Username")
    return '<a href="https://localhost:9110/chat"><p>行こう！</p>'
@bottle.get('/chat')
def chat1():
    global show
    a = '''
    <form action = "/chat" method = "post">
        テキスト : <input name = "texts" type = "text" />
        <input value = "投稿!" type = "submit"/>
    </form>
    '''
    text = show + "\n\r" + a
    return text
@bottle.post('/chat')
def chat2():
    global s,chat,name
    tetx = bottle.request.forms.get("texts")
    data = pickle.dumps(["add",name,tetx])
    if tetx == "reset":
        data = pickle.dumps(["load"])
    s.sendall(data)
    chat = pickle.loads(s.recv(8192))
    show = p(chat)
bottle.run(host='localhost',port=9110)