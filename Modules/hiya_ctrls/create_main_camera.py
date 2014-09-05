# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def create_main_camera(task):
    camera_name = tactic_ctrls.get_task_cam_name(task)
    return maya_ctrls.create_camera(camera_name)