#!/usr/bin/python3
"""
 script (based on the file 1-pack_web_static.py) that distributes an 
 archive to your web servers, using the function do_deploy
 """
from fabric.api import run, env, put
import os.path

def do_deploy(archive_path):
    """ deploy remote servers """
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split('/')[-1]
        file_no_ext = file_name.split('.')[0]
        path = "/data/web_static/releases/"

        env.hosts = ['100.25.134.180', '18.210.16.180']
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_no_ext))
        return True
    except:
        return False

