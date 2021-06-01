# coding: utf-8
import os

from git import Repo
import logging

BASE_DIR = os.path.dirname(__file__)
URL = 'http://hopedong:590221donghP@talkcheap.xiaoeknow.com/hopedong/xiaoe_testing_platform.git'


def clone_pro(url, branch='master'):
    pro_dir = os.path.join(BASE_DIR, 'django_pro')
    if not pro_dir:
        Repo.clone_from(url, pro_dir, branch=branch)
        return True
    else:
        logging.info("[clone_pro] 项目目录已存在")
        return False


if __name__ == '__main__':
    clone_pro(URL)
