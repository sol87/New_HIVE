#coding=utf-8
#__author__ = 'xuguoliang'
#description='''  '''

import os
import sys
from get_parent_dir import get_parent_dir
this_package_path = get_parent_dir()
Moudules_path = get_parent_dir(this_package_path)
sys.path.append(Moudules_path)
from tactic_client_lib import TacticServerStub
from hiya_ctrls import hiya_globals
