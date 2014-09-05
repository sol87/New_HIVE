# coding=utf-8
#__author__ = 'xuguoliang'
#description='''  '''

from sub_importer import *
from create_main_camera import create_main_camera
from set_scene_defaults import set_scene_defaults


def set_task_maya_env(task):
    process = task["process"]
    set_scene_defaults(task["project_code"])
    # temp codes
    if process == "layout":
        create_main_camera(task)
