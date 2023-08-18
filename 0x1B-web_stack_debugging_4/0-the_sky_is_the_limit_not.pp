# traffic on engine x
exec { 'fixing enginex':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# restart engine x
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
