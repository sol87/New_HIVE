# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def init_globals():
    QtGui.qApp.Globals = {}

    
def set_tactic_server_ip(ip):
    if not hasattr(QtGui.qApp, "Globals"):
        init_globals()
    QtGui.qApp.Globals["tactic_server_ip"] = ip


def get_tactic_server_ip():
    return QtGui.qApp.Globals["tactic_server_ip"]


def set_tactic_server(server):
    if not hasattr(QtGui.qApp, "Globals"):
        init_globals()
    QtGui.qApp.Globals["tactic_server"] = server


def get_tactic_server():
    return QtGui.qApp.Globals["tactic_server"]