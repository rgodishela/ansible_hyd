Ansible Installation
************************

*OS: CentOS:7*

$ sudo yum install epel-release || sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ sudo yum update
$ sudo yum install ansible
$ sudo ansible --version

*OS: Ubuntu 17 LTS*

$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
