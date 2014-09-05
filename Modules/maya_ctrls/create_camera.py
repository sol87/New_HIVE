# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def create_camera(name=None):
    this_camera = mc.camera()
    if name:
        return mc.rename(this_camera[0], name)