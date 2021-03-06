#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import quotespd
__author__ = 'wangjj'
__mtime__ = '20161026下午 10:20'


class ChangeDepthDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(ChangeDepthDialog, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((350, 200))
        self.SetTitle("Configure Data")

    def InitUI(self):
        self.option_list = ['open', 'close', 'high', 'low', 'volume']

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        sb = wx.StaticBox(pnl, label='Data Range')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)

        sbs.Add(wx.StaticText(pnl, -1, r'Start Date'))
        self.dc_start = wx.adv.DatePickerCtrl(
            pnl, -1, style=wx.adv.DP_DROPDOWN, pos=(130, 70))
        sbs.Add(self.dc_start)
        sbs.Add(wx.StaticText(pnl, -1, r'End Date'))
        self.dc_end = wx.adv.DatePickerCtrl(
            pnl, -1, style=wx.adv.DP_DROPDOWN, pos=(330, 70))
        sbs.Add(self.dc_end)
        pnl.SetSizer(sbs)

        pnl2 = wx.Panel(self)
        sb2 = wx.StaticBox(pnl2, label='Data Set')
        sbs2 = wx.StaticBoxSizer(sb2, orient=wx.VERTICAL)
        self.cb_list = []
        for l in self.option_list:
            # originally 3 params: style=wx.RB_GROUP
            cb = wx.CheckBox(pnl2, label=l)
            sbs2.Add(cb)
            self.cb_list.append(cb)

        pnl2.SetSizer(sbs2)
        hbox.Add(pnl)
        hbox.Add(pnl2)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(hbox, proportion=1)
        vbox.Add(hbox2,
                 flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnCancel)

    def ShowDialog(self, code1):
        self.code = code1
        self.Show(True)

    def OnClose(self, e):
        l = []
        for i, cb in enumerate(self.cb_list):
            if cb.GetValue():
                l.append(self.option_list[i])
        print (l)
        print (self.code)
        print (self.dc_start.GetValue(), self.dc_end.GetValue())
        if l != []:
            quotespd.PlotData(
                code=self.code,
                start=self.dc_start.GetValue(),
                end=self.dc_end.GetValue(),
                list=l)
            # self.Destroy()

    def OnCancel(self, e):
        self.Close()


def ConfigureData(codes):
    print ("codes in dialogs", codes)
    ex = wx.App()
    print ("retrived the first code", codes[0])
    cd = ChangeDepthDialog(None)
    cd.ShowDialog(codes[0])
    ex.MainLoop()
