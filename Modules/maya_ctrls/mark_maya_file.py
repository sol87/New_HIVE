# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def mark_maya_file(task):
    mc.addAttr(
        "persp", longName="search_code", dataType="string", h=1, w=0)
    mc.setAttr(
        "persp.search_code", task["search_code"]+"_"+task["process"], type="string")
    return True