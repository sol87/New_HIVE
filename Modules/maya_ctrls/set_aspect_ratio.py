# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def set_aspect_ratio(size):
    mc.setAttr("defaultResolution.width",size[0])
    mc.setAttr("defaultResolution.height",size[1])
    deviceAspectRatio = float(size[0])/float(size[1])
    mc.setAttr("defaultResolution.deviceAspectRatio",deviceAspectRatio)
    mc.setAttr("defaultResolution.pixelAspect",1)