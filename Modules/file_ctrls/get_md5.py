# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *


def get_md5(path, block_size=2**20):
    md5 = hashlib.md5()
    f = open(path)
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.close()
    return md5.hexdigest()