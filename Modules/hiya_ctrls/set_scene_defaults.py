# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *
from get_project_configs import get_project_configs


def set_scene_defaults(project):
    scene_configs = get_project_configs(project)
    set_configs = []
    for config in scene_configs:
        if config[0] == "FPS":
            maya_ctrls.set_fps(config[1])
            set_configs.append(config)
        elif config[0] == "aspect_ratio":
            maya_ctrls.set_aspect_ratio(config[1])
            set_configs.append(config)
    return set_configs
