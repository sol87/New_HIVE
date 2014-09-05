# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def set_start_frame(frame):
    mc.playbackOptions(animationEndTime= frame)
    return mc.playbackOptions(maxTime= frame)