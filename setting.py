# MCSMConnect
# 导入库
import tkinter as tk
import os
import tkinter.messagebox
import configparser

setting = tk.Tk()
setting.title('设置')
setting.geometry('500x300')
setting.iconbitmap('./logo.ico')


def print_selection():
    if set1.get() == 1:
        tkinter.messagebox.showinfo(title='成功', message='已经成功开启自动更新，MCSM助手将会在每次启动时自动获取更新！')
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
c1 = tk.Checkbutton(setting, text='启动时检测更新', variable=set1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()

cf = configparser.ConfigParser()
cf.read(".\\config.ini")
au = cf.get("Settings", "autoupdate")

if au == "True":
    c1.select()
else:
    pass


setting.mainloop()
