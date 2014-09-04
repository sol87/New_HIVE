# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *

def get_current_file_name():
    return mc.file(query=True, sceneName=True)