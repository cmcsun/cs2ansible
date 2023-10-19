# cs2ansible
ansible playbook for deploying cs2 servers
 
  
  # todo: add support for plugins sourcemod/metamod
  # todo: make it not necessary to manually login to steamcmd before running the final script cs2update.sh
  # todo: automate tmux and run script automatically (how?)


before running the playbook. user named ansible on master node. user named ansible on slave nodes. each ssh key must be copied before using ansible. the hosts.ini assumes there is no ssh key passphrase. edit accordingly

git clone this repo on master and slave

sudo python create_user_with_sudo.py to create user on slave node -  do on slave (works on Arch, does not work on fedora for some reason)

create ssh key - do on master

edit sshcopyidhosts.ini with hosts to copy ssh key to

python3 copy_ssh_keys.py ansible sshcopyidhosts.ini -  do on master

to run playbook: ansible-playbook cs2_servers.yml -i hosts.ini --ask-become-pass
(can also use ansible secret vault to store password for the ansible user to use sudo access on the box its running on)

will fail here: NO SUCH FILE OR DIRECTORY

run steamcmd

login to user on steamcmd

Delete .steam directory

run playbook again

then edit and launch cs2update.sh


