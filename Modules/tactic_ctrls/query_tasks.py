# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def query_tasks(status, assigned=None):
    server = hiya_ctrls.hiya_globals.get_tactic_server()
    if assigned:
        return server.query("sthpw/task", filters=[("status", status), ("assigned", assigned), ("project_code", server.project_code)])
    else:
        return server.query("sthpw/task", filters=[("status", status), ("project_code", server.project_code)])
