# MCSMConnect
# 导入库
import tkinter as tk
import tkinter.messagebox
import os
import configparser
import requests
import sys
import json
import urllib.parse
import urllib.request
import zipfile
import threading
import time

# 创建所需程序所需的文件夹
# file2 = os.path.exists(".\\update\\")
# if not file2:
#    os.mknod("test.txt")

if not os.path.isfile('.\\config.ini'):
    tkinter.messagebox.showerror(title='错误', message='检测到缺少文件，软件自动下载缺少的文件')
    configd = 'http://update.mcbeserver.cn:333/MCSMTools/config.ini'
    cfd = requests.get(configd)
    with open("config.ini", "wb") as code:
        code.write(cfd.content)
else:
    pass

if not os.path.isfile('.\\update.exe'):
    tkinter.messagebox.showerror(title='错误', message='检测到缺少文件，软件自动下载缺少的文件')
    udd = 'http://update.mcbeserver.cn:333/MCSMTools/update.exe'
    ud = requests.get(udd)
    with open("update.exe", "wb") as udf:
        udf.write(ud.content)
else:
    pass

if not os.path.isfile('.\\logo.ico'):
    tkinter.messagebox.showerror(title='错误', message='检测到缺少文件，软件自动下载缺少的文件')
    icod = 'http://update.mcbeserver.cn:333/MCSMTools/logo.ico'
    icd = requests.get(icod)
    with open("logo.ico", "wb") as code:
        code.write(icd.content)
else:
    pass

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

    tkinter.messagebox.showinfo(title='成功', message='信息保存成功，为您跳转到主界面')
    mcsm.destroy()
    main = tk.Tk()
    main.title('MCSMTools')
    main.geometry('500x250')
    main.iconbitmap('./logo.ico')

    # 更新代码
    cf = configparser.ConfigParser()
    cf.read(".\\config.ini")
    au = cf.get("Settings", "autoupdate")

    vs = requests.get("http://update.mcbeserver.cn:333/MCSMTools/version.html")

    vc = configparser.ConfigParser()
    vc.read(".\\config.ini")
    nvs = vc.get("Other", "version")

    if au == "True":
        if vs.text != nvs:
            os.system('update.exe')
        else:
            pass
    else:
        pass

    sh = configparser.ConfigParser()
    sh.read(".\\config.ini")
    seth = sh.get("MCSM", "http")

    sk = configparser.ConfigParser()
    sk.read(".\\config.ini")
    setk = sk.get("MCSM", "key")

    srn = configparser.ConfigParser()
    srn.read(".\\config.ini")
    sets = sk.get("MCSM", "server")

    def sethk():
        mcsm = tk.Toplevel()
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

    def setting():
        setting = tk.Toplevel()
        setting.title('设置')
        setting.geometry('500x300')
        setting.iconbitmap('./logo.ico')

        def print_selection():
            if set1.get() == 1:
                tkinter.messagebox.showinfo(title='成功', message='已经成功开启自动更新，MCSM助手将会在每次启动时自动获取更新并安装！')
                cff1 = configparser.ConfigParser()
                cff1.read(".\\config.ini")
                cff1.set("Settings", "autoupdate", "True")
                with open(".\\config.ini", "w+") as f1:
                    cff1.write(f1)
            else:
                cff2 = configparser.ConfigParser()
                cff2.read(".\\config.ini")
                cff2.set("Settings", "autoupdate", "False")
                with open(".\\config.ini", "w+") as f2:
                    cff2.write(f2)

        set1 = tk.IntVar()
        c1 = tk.Checkbutton(setting, text='自动更新', variable=set1, onvalue=1, offvalue=0, command=print_selection)
        c1.pack()

        cf = configparser.ConfigParser()
        cf.read(".\\config.ini")
        au = cf.get("Settings", "autoupdate")

        if au == "True":
            c1.select()
        else:
            pass

        setting.mainloop()

    def about():
        tkinter.messagebox.showinfo(title='关于', message='软件版本 : 1.0.2\n'
                                                        'By DongShao\n'
                                                        'Update API:\n'
                                                        'update.mcbeserver.cn:333/MCSMCTools/\n'
                                                        'QQ群：159323818')

    def new():
        tkinter.messagebox.showinfo(title='版本', message='软件版本 : 1.0.2\n'
                                                        '最新版本 : ' + vs.text)

    def toss():
        response = requests.get(seth + 'api/start_server/' + sets,
                                params={
                                    'apikey': setk
                                },
                                headers={
                                    'User-Agent': 'MCSMTools',
                                })
        zj = json.loads(response.text)

        if zj['status'] == 200:
            tkinter.messagebox.showinfo(title='成功', message='开启成功' + '。状态码：' + str(zj['status']))
        else:
            tkinter.messagebox.showerror(title='错误', message=zj['error'] + '。状态码：' + str(zj['status']))

    def tosts():
        response = requests.get(seth + 'api/stop_server/' + sets,
                                params={
                                    'apikey': setk
                                },
                                headers={
                                    'User-Agent': 'MCSMTools',
                                })

        zj = json.loads(response.text)

        if zj['status'] == 200:
            tkinter.messagebox.showinfo(title='成功', message='关闭成功。状态码：' + str(zj['status']))
        else:
            tkinter.messagebox.showerror(title='错误', message=zj['error'] + '。状态码：' + str(zj['status']))

    def toses():
        response = requests.post(seth + 'api/execute/',
                                 params={
                                     'apikey': setk
                                 },
                                 data={
                                     'name': sets,
                                     'command': sendcommand.get()
                                 },
                                 headers={
                                     'User-Agent': 'MCSMTools',
                                 })
        zj = json.loads(response.text)
        if zj['status'] == 200:
            tkinter.messagebox.showinfo(title='成功', message='发送成功' + '。状态码：' + str(zj['status']))
        else:
            tkinter.messagebox.showerror(title='错误', message=zj['error'] + '。状态码：' + str(zj['status']))

    starts = tk.Button(main, text='开启服务器', font=('Arial', 12), width=1000, height=3, command=toss)
    starts.pack()
    stops = tk.Button(main, text='关闭服务器', font=('Arial', 12), width=1000, height=3, command=tosts)
    stops.pack()
    sendcommand = tk.StringVar(value='要发送的指令(不用/)')
    sendc = tk.Entry(main, show=None, font=('Arial', 14), width=1000, textvariable=sendcommand)
    sendc.pack()
    sends = tk.Button(main, text='发送指令到服务器', font=('Arial', 12), width=1000, height=3, command=toses)
    sends.pack()

    # 菜单
    menu = tk.Menu(main)
    control = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label='操作', menu=control)
    helpa = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label='帮助', menu=helpa)
    helpa.add_command(label='关于', command=about)
    helpa.add_command(label='版本', command=new)
    control.add_command(label='面板信息', command=sethk)
    control.add_command(label='设置', command=setting)

    def my_close():
        sys.exit(0)

    main.protocol('WM_DELETE_WINDOW', my_close)

    main.config(menu=menu)


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


def my_close():
    sys.exit(0)


mcsm.protocol('WM_DELETE_WINDOW', my_close)

mcsm.mainloop()
