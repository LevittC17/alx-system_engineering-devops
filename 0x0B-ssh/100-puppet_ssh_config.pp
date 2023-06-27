# Client configuration with Puppet

file { 'PasswordAuthentication':
  ensure  => file
  path    => '/etc/ssh/ssh_config'
  content => '
    Host 122750-web-01
        HostName 18.207.140.105
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ',
}
