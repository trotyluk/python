#!Python3
# to run programm needs 7z on linux or mac or 7z.exe on Windows

import fnmatch
import argparse
import os
import re
import sys
import shutil
import platform
import socket
import pathlib

def check_os():
    """Function check OS."""
    my_system = platform.uname()
    system = my_system.system
    node = my_system.node
    release = my_system.release
    version = my_system.version
    machine = my_system.machine
    processor = my_system.processor
    config = [system,node,release,version,machine,processor]
    return config

#NOTE - Program Start
#NOTE - check system
print(check_os())
#NOTE - check 7z

