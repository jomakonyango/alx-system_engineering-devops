# File: modules/nginx_config/manifests/init.pp

# Class: nginx_config
# This class manages the nginx configuration and service.

class nginx_config {
  # Ensure the nginx service is running and enabled
  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  # Set worker_processes in nginx.conf to 'auto'
  file_line { 'nginx_worker_processes':
    path   => '/etc/nginx/nginx.conf',
    line   => 'worker_processes auto;',
    match  => '^worker_processes',
    notify => Service['nginx'],
  }

  # Set worker_connections in nginx.conf to '1024'
  file_line { 'nginx_worker_connections':
    path   => '/etc/nginx/nginx.conf',
    line   => 'worker_connections 1024;',
    match  => '^worker_connections',
    notify => Service['nginx'],
  }

  # Set keepalive_timeout in nginx.conf to '65'
  file_line { 'nginx_keepalive_timeout':
    path   => '/etc/nginx/nginx.conf',
    line   => 'keepalive_timeout 65;',
    match  => '^keepalive_timeout',
    notify => Service['nginx'],
  }
}

include nginx_config

