# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def open_maya_file(file_name):
    mc.file(file_name, open=True, force=True)