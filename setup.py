# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:34:40 2022

@author: luigi
"""

import sqlite3


con = sqlite3.connect('chat.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS texts")
cur.execute("CREATE TABLE texts \
            (name TEXT PRIMARY KEY,seid TEXT)")
con.commit()
con.close()