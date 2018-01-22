# encoding=utf8
'''
Created on 2016-08-18

@author: jingyang <jingyang@nexa-corp.com>

Usage:
    fab staging deploy
    fab prod deploy
'''
from fabric.api import local
from fabric.context_managers import lcd, cd
from fabric.operations import put, run
from fabric.state import env
import os
# import wingdbstub

PROJECT_NAME = "liantang"
PROJECT_DIR = "/pypro/liantang"  # project dir on server
with_helpers=True

local_dir= os.path.dirname(os.path.dirname(__file__))

def staging():
    env.user = "root"
    env.hosts = ["prototype.enjoyst.com"]


def prod():
    env.user = "develop"
    env.hosts = ["10.0.2.253"]


def archive(path,name):
    deploy_dir = os.path.join(local_dir,'deploy')
    tar_file = os.path.join(deploy_dir,name+'.tar.gz') #'deploy/liantang.tar.gz' #
    
    with lcd(path):
        local("git archive -o %s HEAD"%tar_file)


def upload(name):
    with cd(PROJECT_DIR):
        put("{}.tar.gz".format(name), ".")


def extract(name,dst):
    with cd(PROJECT_DIR):
        run("tar xf {}.tar.gz -C {}".format(name,dst))


def deploy():
    run('mkdir %s'%PROJECT_DIR)
    
    archive(local_dir,PROJECT_NAME)
    upload(PROJECT_NAME)
    extract(PROJECT_NAME,PROJECT_DIR)
    
    if with_helpers:
        helper_path=os.path.join(local_dir,'src/helpers')
        archive(helper_path,'helpers')
        upload('helpers')
        extract('helpers',os.path.join(PROJECT_DIR,'src/helpers'))
