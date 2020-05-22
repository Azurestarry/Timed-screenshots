#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author1__ = 'jethro'
__author2__ = 'Azure_starry'

DELAY = 600 # seconds

import os
import wx
import time
import wx.adv
import _thread
from PIL import ImageGrab

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "time.ico"
    ID_ABOUT = wx.NewIdRef()
    ID_EXIT = wx.NewIdRef()
    ID_SHOW_WEB = wx.NewIdRef()
    TITLE = "Timed Screenshot"

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)
        self.Bind(wx.EVT_MENU, self.onAbout, id = self.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.onExit, id = self.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onShowWeb, id = self.ID_SHOW_WEB)
        try:
            _thread.start_new_thread(take_screenshots, (DELAY, ))
        except:
            wx.MessageBox('[Error]: Unable to start new thread', "Message")

    def onAbout(self, event):
        wx.MessageBox('Authors: Jethro & Azure_starry', "About")

    def onExit(self, event):
        wx.Exit()

    def onShowWeb(self, event):
        # print('Show Web')
        os.system('start explorer .\\Screenshots\\')

    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    def getMenuAttrs(self):
        return [('Open Folder', self.ID_SHOW_WEB),
                ('About', self.ID_ABOUT),
                ('Exit', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True

def check_path():
    if not os.path.exists('./Screenshots/'):
        os.makedirs('./Screenshots/')

def take_screenshot():
    ctime = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
    ts = ImageGrab.grab()
    ts.save('./Screenshots/' + ctime + '.png')

def take_screenshots(delay):
    take_screenshot()
    time.sleep(delay)
    _thread.start_new_thread(take_screenshots, (delay, ))

if __name__ == "__main__":

    check_path()

    # take_screenshot()

    app = MyApp()
    app.MainLoop()
