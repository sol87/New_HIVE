# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def reference_maya_file(file_name):
    return mc.file(file_name, reference=True, force=True)
