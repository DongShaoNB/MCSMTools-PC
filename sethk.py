# MCSMConnect
# 导入库
import tkinter as tk
import tkinter.messagebox
import os
import configparser
import requests

# 设置窗口基本信息

mcsm = tk.Tk()
mcsm.title('MCSM信息填写')
mcsm.geometry('400x190')
mcsm.iconbitmap('./logo.ico')


# 函数执行
def saveinfo():
    http = configparser.ConfigParser()
    http.read(".\\config.ini")
    http.set("MCSM", "http", htt.get())
    with open(".\\config.ini", "w+") as h:
        http.write(h)

    key = configparser.ConfigParser()
    key.read(".\\config.ini")
    key.set("MCSM", "key", ke.get())
    with open(".\\config.ini", "w+") as y:
        key.write(y)

    snsn = configparser.ConfigParser()
    snsn.read(".\\config.ini")
    snsn.set("MCSM", "server", servern.get())
    with open(".\\config.ini", "w+") as s:
        snsn.write(s)

    tkinter.messagebox.showinfo(title='成功', message='信息保存成功')
    mcsm.destroy()


sh = configparser.ConfigParser()
sh.read(".\\config.ini")
seth = sh.get("MCSM", "http")

sk = configparser.ConfigParser()
sk.read(".\\config.ini")
setk = sk.get("MCSM", "key")

srn = configparser.ConfigParser()
srn.read(".\\config.ini")
sets = sk.get("MCSM", "server")

# 设置控件
t1 = tk.Label(mcsm, text='请填写您的MCSM信息', bg='red', font=('Arial', 20), width=1000, height=2)
t1.pack()

htt = tk.StringVar(value=seth)
ht = tk.Entry(mcsm, show=None, font=('Arial', 14), width=1000, textvariable=htt)
ht.pack()

ke = tk.StringVar(value=setk)
k = tk.Entry(mcsm, show=None, font=('Arial', 14), width=1000, textvariable=ke)
k.pack()

servern = tk.StringVar(value=sets)
sn = tk.Entry(mcsm, show=None, font=('Arial', 14), width=1000, textvariable=servern)
sn.pack()

qd = tk.Button(mcsm, text='保存信息', font=('Arial', 14), width=1000, height=2, command=saveinfo)
qd.pack()

mcsm.mainloop()
