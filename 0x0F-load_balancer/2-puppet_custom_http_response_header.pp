#!/usr/bin/python3
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to include custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                
                location / {
                  add_header X-Served-By $hostname;
                  root /var/www/html;
                  index index.html index.htm;
                }
            }",
  notify  => Service['nginx'],
}

# Enable the default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service whenever the configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
