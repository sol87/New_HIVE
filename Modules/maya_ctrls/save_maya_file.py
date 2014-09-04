# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def save_maya_file(name):
    mc.file(rename=name)
    mc.file(save=True)
