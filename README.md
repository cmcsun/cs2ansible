# cs2ansible
ansible playbook for deploying cs2 servers
 
  
  # todo: add support for plugins sourcemod/metamod
  # todo: make it not necessary to manually login to steamcmd before running the final script cs2update.sh
  # todo: automate tmux and run script automatically (how?)


before running the playbook. user named ansible on master node. user named ansible on slave nodes. each ssh key must be copied before using ansible. the hosts.ini assumes there is no ssh key passphrase. edit accordingly

sudo python create_user_with_sudo.py to create user on slave node

python3 copy_ssh_keys.py ansible sshcopyidhosts.ini

to run playbook: ansible-playbook cs2_servers.yml -i hosts.ini --ask-become-pass

can also use ansible secret vault to store password for the ansible user to use sudo access on the box its running on
