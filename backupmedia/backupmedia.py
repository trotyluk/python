#!python3
import os
import platform
# lista katalogów
# check operating system
def check_os():
    my_system = platform.uname()
    system = my_system.system
    node = my_system.node
    release = my_system.release
    version = my_system.version
    machine = my_system.machine
    processor = my_system.processor
    config = [system,node,release,version,machine,processor]
    # return configuration in the list format
    # [system,node,release,version,machine,processor]
    return config

print(check_os())
