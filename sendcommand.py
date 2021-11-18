import tkinter as tk
import tkinter.messagebox
import os
import configparser
import requests
import sys
import urllib.parse
import urllib.request
import json

sc = tk.Tk()
sc.title('发送指令到服务器')
sc.geometry('300x80')
sc.iconbitmap('./logo.ico')

sh = configparser.ConfigParser()
sh.read(".\\config.ini")
seth = sh.get("MCSM", "http")

sk = configparser.ConfigParser()
sk.read(".\\config.ini")
setk = sk.get("MCSM", "key")

srn = configparser.ConfigParser()
srn.read(".\\config.ini")
sets = sk.get("MCSM", "server")


def scm():
    response = requests.post(seth + 'api/execute/',
                             params={
                                 'apikey': setk
                             },
                             data={
                                 'name': sets,
                                 'command': cm.get()
                             },
                             headers={
                                 'User-Agent': 'MCSMTools',
                             })
    zj = json.loads(response.text)
    if zj['status'] == 200:
        tkinter.messagebox.showinfo(title='成功', message='发送成功' + '。状态码：' + str(zj['status']))
    else:
        tkinter.messagebox.showerror(title='错误', message=zj['error'] + '。状态码：' + str(zj['status']))


cm = tk.StringVar(value='请输入指令(无需/)')
command = tk.Entry(sc, show=None, font=('Arial', 14), width=1000, textvariable=cm)
command.pack()

send = tk.Button(sc, text='发送指令', font=('Arial', 14), width=1000, height=2, command=scm)
send.pack()

sc.mainloop()
