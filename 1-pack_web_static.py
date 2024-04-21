#!/usr/bin/python3
# Fabfile to generates .tgz archive from the contents of
# web_static directory

import os.path
from datetime import datetime
from fabric


def do_pack():
    """Creates a tar gzipped archive of web_static directory"""
    dt = datetime.utcnow()
    file = f"versions/web_static_{dt.year}{dt.month}{dt.day}\
                                    {dt.hour}{dt.minute}{dt.second}.tgz"
    if not os.path.isdir("versions") or local("mkdir -p versions").failed:
        return None
    if local(f"tar -cvzf {file} web_static").failed:
        return None
    return file

if __name__ == "__main__":
    do_pack()
