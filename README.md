# cs2ansible
ansible playbook for deploying cs2 servers
 
  
  # todo: add support for plugins sourcemod/metamod
  # todo: add create user for steamuser
  # todo: automate tmux and run script automatically (how?)
  # todo: python script to run on fresh server slave to create ansible user and edit visudo /etc/sudoers with ansible user in wheel.
  # todo: python script to run on server master to copy ssh id to hosts in hosts.ini


before running the playbook. user named ansible on master node. user named ansible on slave nodes. each ssh key must be copied before using ansible. the hosts.ini assumes there is no ssh key passphrase. edit accordingly

to run playbook: ansible-playbook cs2_servers.yml -i hosts.ini --ask-become-pass

can also use ansible secret vault to store password for the ansible user to use sudo access on the box its running on
