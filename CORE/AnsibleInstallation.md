 # Ansible Installation
************************

## CentOS:7

```sh
sudo yum install epel-release 

(or)

sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum update
sudo yum install ansible
sudo ansible --version
```
## Ubuntu 17 LTS

```sh
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
sudo ansible --version
```
