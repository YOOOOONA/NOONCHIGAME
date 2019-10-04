# -*- coding: utf-8 -*-
activate_this = "/home/ec2-user/venv/python36/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0,'/home/ec2-user/venv/project/FourBoxes')
from __init__ import app as application

