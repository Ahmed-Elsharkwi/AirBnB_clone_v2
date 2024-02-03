#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""
file_1 = __import__("1-pack_web_static")
file_2 = __import__("2-do_deploy_web_static")


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = file_1.do_pack()
    if archive_path is None:
        return False
    return file_2.do_deploy(archive_path)
