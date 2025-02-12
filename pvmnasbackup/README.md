# pvm-backup

backup pvm virtual machine and transport to nas
Parallels write wirtual machines into *.pvm directories so that program
create 7zip archive for every *.pvm directory and sending them with scp command through ssh into NAS

## In program you need to set variables

1. NAS IP
2. ssh port
3. Target directory on NAS
