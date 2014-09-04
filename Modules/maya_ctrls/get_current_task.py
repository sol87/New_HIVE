# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def get_current_task():
    try:
        return mc.getAttr('persp.search_code')
    except:
        return