#!/usr/bin/python2.7
import os,sys
import shutil
from app.models import basedir,basedir2, showvalues,site_info
from config import Config


datadir = "/tmp/data.json"
datadir2 = "/tmp/data2.json"

showvalues(datadir,int(sys.argv[1]))
site_info(datadir2,int(sys.argv[1]))
if os.path.exists(datadir):
    os.remove(basedir)
if os.path.exists(datadir2):
    os.remove(basedir2)
shutil.move(datadir, basedir)
shutil.move(datadir2, basedir2)
