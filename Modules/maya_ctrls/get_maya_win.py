#coding=utf-8
#__author__ = 'xuguoliang'
#description='''  '''

from sub_importer import *


def get_maya_win():
    prt = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(prt),QtGui.QWidget)