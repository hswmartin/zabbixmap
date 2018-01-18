import json
import urllib2
from config import Config
import os
import re


basedir = os.path.abspath(os.path.dirname(__file__)) + "/templates/data.json"
basedir2 = os.path.abspath(os.path.dirname(__file__)) + "/templates/data2.json"

def getgrouplist():
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": ["groupid", "name"],
            },
            "auth": Config.hash_password,
            "id": 1,
        })
    request = urllib2.Request(Config.url, data)
    for key in Config.header:
        request.add_header(key, Config.header[key])
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()
    return response['result']


def gethostlist(groupid):
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid", "name"],
                "groupids": groupid,
            },
            "auth": Config.hash_password,
            "id": 1,
        })
    request = urllib2.Request(Config.url, data)
    for key in Config.header:
        request.add_header(key, Config.header[key])
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()
    listofhost = {}
    for host in response['result']:
        listofhost[host['name']] = host['hostid']
    return listofhost


def getitemlist(hostid):
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": ["itemids", "key_"],
                "hostids": hostid,
            },
            "auth": Config.hash_password,
            "id": 1,
        })
    request = urllib2.Request(Config.url, data)
    for key in Config.header:
        request.add_header(key, Config.header[key])
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()
    listofitem = {}
    for item in response['result']:
        listofitem[item['key_']] = item['itemid']
    return listofitem


def getitemvalue(keyid):
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                "output": "extend",
                "history": 3,
                "itemids": keyid,
                "sortfield": "clock",
                "sortorder": "DESC",
                "limit": 1,
            },
            "auth": Config.hash_password,
            "id": 1,
        })
    request = urllib2.Request(Config.url, data)
    for key in Config.header:
        request.add_header(key, Config.header[key])
    result = urllib2.urlopen(request)
    response = json.loads(result.read())
    result.close()
    valueofkey = {}
    for key in response['result']:
        valueofkey[key['itemid']] = key['value']
    return valueofkey


def secondtoday(seconds):
    minute = (int(seconds) / 60) % 60
    hour = ((int(seconds) / 60) / 60) % 24
    day = ((int(seconds) / 60) / 60) / 24
    return [minute, hour, day]

def site_info(datadir,n):
    site_info = []
    for site in Config.site_info[n]:
        site_info.append(site)
    json.dump(site_info, open(datadir, 'w'))

def showvalues(datadir,n):
    listofgroup = {}
    for groupid in Config.groupid:
        hostlist = gethostlist(groupid)
        listofhost = []
        for hostname in Config.listofhost[n]:
            listofitem = []
            listofnetwork = []
            listofnetworkin = []
            networkflow = 0
            networkflowin = 0
            hostid = hostlist[hostname]
            itemlist = getitemlist(hostid)
            for itemkey in itemlist.keys():
                networkout = re.match(r'net.if.out\[.*', itemkey)
                networkin = re.match(r'net.if.in\[.*', itemkey)
                if itemkey == 'system.uptime':
                    itemid = itemlist[itemkey]
                    itemvalue = getitemvalue(itemid)
                    if itemvalue:
                        listofitem.append(itemvalue[itemid])
                    else:
                        listofitem.append('0')
                elif itemkey == 'icmpping' or itemkey == 'agent.ping':
                    itemid = itemlist[itemkey]
                    itemvalue = getitemvalue(itemid)
                    if itemvalue:
                        listofitem.append(itemvalue[itemid])
                    else:
                        listofitem.append('0')
                elif networkout:
                    itemid = itemlist[itemkey]
                    itemvalue = getitemvalue(itemid)
                    if itemvalue:
                        listofnetwork.append(itemvalue[itemid])
                    else:
                        listofnetwork.append('0')
                elif networkin:
                    itemid = itemlist[itemkey]
                    itemvalue = getitemvalue(itemid)
                    if itemvalue:
                        listofnetworkin.append(itemvalue[itemid])
                    else:
                        listofnetworkin.append('0')
                else:
                    continue
            for i in range(0, len(listofnetwork)):
                networkflow += int(listofnetwork[i])
            for i in range(0, len(listofnetworkin)):
                networkflowin += int(listofnetworkin[i])
            listofitem.append(networkflow / 1024 / 1024.00)
            listofitem.append(networkflowin / 1024 / 1024.00)
            listofhost.append(listofitem)
        listofgroup[groupid] = listofhost
    json.dump(listofgroup, open(datadir, 'w'))
