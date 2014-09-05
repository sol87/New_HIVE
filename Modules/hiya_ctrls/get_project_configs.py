# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def get_project_configs(project):
    ini_file = os.path.join(Configs_path, "Project_Configs.ini")
    ini_file = r"%s" % ini_file
    all_configs = dict4ini.DictIni(ini_file)
    project_configs = all_configs[project]
    return project_configs