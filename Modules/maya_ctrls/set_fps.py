# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def set_fps(unit):
    result = mc.currentUnit(time= unit)
    current_time = mc.currentTime(query=True)
    mc.currentTime(int(current_time))
    return result