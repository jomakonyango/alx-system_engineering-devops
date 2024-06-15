# 0-the_sky_is_the_limit_not.pp
# This manifest is intended to fix failed requests by optimizing nginx configuration
# and ensuring the nginx service is running with the new configuration.

class nginx_config {
  service { 'nginx':
    ensure => running,
    enable => true,
    subscribe => Exec['fix--for-nginx'],
  }

  exec { 'fix--for-nginx':
    command => '/usr/bin/fix_nginx_config.sh',
    path    => ['/bin', '/usr/bin'],
    refreshonly => true,
  }

  file_line { 'nginx_worker_processes':
    path => '/etc/nginx/nginx.conf',
    line => 'worker_processes auto;',
    match => '^worker_processes',
    notify => Service['nginx'],
  }

  file_line { 'nginx_worker_connections':
    path => '/etc/nginx/nginx.conf',
    line => 'worker_connections 1024;',
    match => '^worker_connections',
    notify => Service['nginx'],
  }

  file_line { 'nginx_keepalive_timeout':
    path => '/etc/nginx/nginx.conf',
    line => 'keepalive_timeout 65;',
    match => '^keepalive_timeout',
    notify => Service['nginx'],
  }
}

include nginx_config
