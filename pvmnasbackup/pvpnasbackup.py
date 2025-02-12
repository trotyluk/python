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
def create_archve(archname):
    #pvmlist= fnmatch.filter(os.listdir('.'), '*pvm')
    create7z='7z a "'+ archname +'.7z" "'+ archname + '"'
    # print(f'Creating {archname}.7z')
    os.system(create7z)
#NOTE - Program Start
#NOTE - check system
osreport=check_os()
systype=osreport[0]
print(systype)
#NOTE - check 7z
