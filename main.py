# coding: utf-8
import logging
import os

from dotenv import load_dotenv
from git import Repo

import subprocess
import shlex

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(module)s - %(lineno)d - %(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(__file__)
URL = os.getenv('URL')


def clone_pro(url, branch='main'):
    if not URL:
        raise EnvironmentError('请配置环境变量：URL')
    pro_dir = os.path.join(BASE_DIR, 'django_pro')
    if not os.path.exists(pro_dir):
        os.mkdir(pro_dir)
        Repo.clone_from(url, pro_dir, branch=branch)
        return True
    else:
        logger.info("[clone_pro] 项目目录已存在")
        return False


def build_project():
    """
    构建项目
    :return:
    """
    if not os.path.exists(os.path.join(BASE_DIR, 'django_pro', 'requirements-prod.txt')):
        raise EnvironmentError('请配置项目的: requirements-prod.txt')
    popenargs = shlex.split('docker-compose build')
    subprocess.run(popenargs)


def up_project():
    """
    启动项目
    :return:
    """


def down_project():
    """
    停止项目
    :return:
    """


if __name__ == '__main__':
    # clone_pro(URL)
    build_project()