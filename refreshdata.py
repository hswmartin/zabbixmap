#!/usr/bin/python2.7
import os,sys
import shutil
from app.models import basedir,basedir2, showvalues,site_info
from config import Config


datadir = "/tmp/data.json"
datadir2 = "/tmp/data2.json"

showvalues(datadir,int(sys.argv[1]))
site_info(datadir2,int(sys.argv[1]))

shutil.copyfile(datadir, basedir)
shutil.copyfile(datadir2, basedir2)
