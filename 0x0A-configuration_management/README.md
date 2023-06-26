### 0x0A. Configuration management

Resources

1. [Intro to Configuration Managemenet](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
2. [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://www.puppet.com/docs/puppet/5.5/types/file.html)
3. [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
4. [Puppet lint](http://puppet-lint.com/)
5. [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)


Tasks


0. Create a file

* Using Puppet, create a file in /tmp.

* Requirements:
	. File path is /tmp/school
	. File permission is 0744
	. File owner is www-data
	. File group is www-data
	 .File contains I love Puppet

1. Install a package

* Using Puppet, install flask from pip3.

* Requirements:
	. Install flask
	. Version must be 2.1.0

Example
```
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

2. Execute a command

* Using Puppet, create a manifest that kills a process named killmenow.

* Requirements:
	. Must use the exec Puppet resource
	. Must use pkill
Example:
	> Terminal #0 - starting my process
