import os.path
import configparser

app = []

host=None
post=None

conf_file = 'config.ini'
conf = configparser.ConfigParser()


def init():
    global conf
    if not os.path.isfile('config.conf'):
        conf['server'] = {'host': '127.0.0.1', 'port': '8080'}
        save()
    else:
        conf.read(conf_file, encoding="utf-8-sig")
    load()


def load():
    global host
    global port
    host = conf.get('server', 'host')
    port = conf.get('server', 'port')

def save():
    global conf
    global host
    global port
    if host and port:
        conf.set('server', 'host', host)
        conf.set('server', 'port', port)
        with open(conf_file, 'w', encoding='utf-8') as _f:
            conf.write(_f)


init()
