# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def new_maya_file(file_name):
    return mc.file(new=True, force=True)
    mc.file(rename=file_name)
    mc.file(save=True, type="mayaAscii", force=True)