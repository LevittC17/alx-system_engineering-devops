# Client configuration file (w/ Puppet)

file_line { 'ssh_config':
  path    => '/etc/ssh/ssh_config',
  line    => [
    Host 122750-web-01,
        HostName 18.207.140.105,
        User ubuntu,
        IdentityFile ~/.ssh/school,
        PreferredAuthentications publickey,
        PasswordAuthentication no,
  ],
  ensure  => present,
  match   => ^Host 122750-web-01$,
}
