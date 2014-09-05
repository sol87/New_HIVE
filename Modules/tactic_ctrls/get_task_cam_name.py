# coding=utf-8
#__author__ = 'xuguoliang'
# description='''  '''

from sub_importer import *


def get_task_cam_name(task):
    naming = get_camera_naming(task["project_code"])
    key_words = [i.split("}")[0] for i in naming.split("{")[1:]]
    conditions = []
    for key_word in key_words:
        conditions.append("{0} = task['{0}']".format(key_word))
    eval_str = "naming.format(%s)" % ",".join(conditions)
    return eval(eval_str)


def get_camera_naming(project):
    configs = hiya_ctrls.get_project_configs(project)
    naming = configs["camera_naming"]
    return naming

