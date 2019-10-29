# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:50:59 2019

@author: 은비
"""

from FourBoxes import app


import threading
from datetime import datetime
from glob import glob

"""
def set_interval(func, sec):
    def func_wrapper(): 
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def a():
    now = datetime.now()
    h = now.hour
    m = now.minute
    if(h==0):
        print(m)
        file = glob("/home/ec2-user/venv/project/FourBoxes/__init__.py")
        for f in file:
            exec(open(f, encoding='UTF-8').read())
        set_interval(a, 3600)
    else : 
        print(m)
        set_interval(a, 3600)

set_interval(a, 60)
"""

app.run(host='0.0.0.0',port=80,debug=True, use_reloader=False) #127.0.0.1 == localhost

