file { '/home/vagrant/.ssh/config':
  ensure => file,
  mode   => '0600',
  content => '
Host *
    Hostname 18.207.140.105
    user ubuntu
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
',
}
