import tkinter as tk
import os
import configparser
import tkinter.messagebox
import requests
import urllib.parse
import urllib.request
import json
import sys

main = tk.Tk()
main.title('MCSMTools')
main.geometry('500x224')
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
        tkinter.messagebox.showinfo(title='更新', message='有新的版本可以更新！我们将自动为您下载到软件根目录，请自行解压覆盖文件('
                                                        '覆盖后配置将会清除，请提前备份config.ini的配置！)')
        ud = 'http://update.mcbeserver.cn:333/MCSMTools/new_' + vs.text + '.zip'
        uud = requests.get(ud)
        with open('new_' + vs.text + '.zip', "wb") as udw:
            udw.write(uud.content)
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
    os.system('python sethk.py')


def setting():
    os.system('python setting.py')


def about():
    tkinter.messagebox.showinfo(title='关于', message='软件版本 : 1.0.0\n'
                                                    'By DongShao\n'
                                                    'Update API:\n'
                                                    'update.mcbeserver.cn:333/MCSMCTools/')


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
    os.system('python sendcommand.py')


starts = tk.Button(main, text='开启服务器', font=('Arial', 12), width=1000, height=3, command=toss)
starts.pack()
stops = tk.Button(main, text='关闭服务器', font=('Arial', 12), width=1000, height=3, command=tosts)
stops.pack()
sends = tk.Button(main, text='发送指令到服务器', font=('Arial', 12), width=1000, height=3, command=toses)
sends.pack()

# 菜单
menu = tk.Menu(main)
control = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='操作', menu=control)
helpa = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='帮助', menu=helpa)
helpa.add_command(label='关于', command=about)
control.add_command(label='面板信息', command=sethk)
control.add_command(label='设置', command=setting)


def my_close():
    sys.exit(0)


main.protocol('WM_DELETE_WINDOW', my_close)

main.config(menu=menu)

