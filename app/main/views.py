# -*- coding: utf-8 -*

from flask import render_template
from . import main
from ..models import showvalues, basedir,basedir2,site_info
from config import Config
import os
import json


@main.route('/')
def zabbixmap():
    if os.path.exists(basedir) and os.path.exists(basedir2):
        pass
    else:
        showvalues(basedir,0)
        site_info(basedir2, 0)
    showvalue = json.dumps(json.load(open(basedir, 'r')))
    site_info = json.dumps(json.load(open(basedir2, 'r')))
    return render_template("index.html", site_info=site_info, showvalue=showvalue)
@main.route('/rr')
def rr():
    if os.path.exists(basedir) and os.path.exists(basedir2):
        pass
    else:
        showvalues(basedir,0)
        site_info(basedir2, 0)
    showvalue = json.dumps(json.load(open(basedir, 'r')))
    site_info = json.dumps(json.load(open(basedir2, 'r')))
    return render_template("rr.html", site_info=site_info, showvalue=showvalue)
if __name__ == "__main__":
    app.run()
