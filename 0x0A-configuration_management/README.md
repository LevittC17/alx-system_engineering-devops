### 0x0A. Configuration management

# Installing puppet
	$ apt-get install -y ruby=1.2.7+1 --allow-downgrades
	$ apt-get install -y ruby-augeas
	$ apt-get install -y ruby-shadow
	$ apt-get install -y puppet

# Installing puppet-init
	$ gem install puppet-init

Tasks / Guidance

# 0. Create File

_using puppet, create a file in /tmp

Requirements:
    _ File Path /tmp/school
    _ File Permission - 0744
    _ File Owner - www-data
    _ File Group - www-data
    _ File Contains - I love Puppet

folder name: 0x0A-configuration_management
file name: 0-create_a_file.pp


## 1. Install a package

* Using puppet, install flask from pip3
* Requirements:
	*** Instal flask
	*** Version must be 2.1.0


## 2. Execute a command

* Using puppet, create a manifest that kills a process named killmenow
* Requirements:
	*** Must be the 'exec' Puppet resource
	*** Must use 'pkill'

















