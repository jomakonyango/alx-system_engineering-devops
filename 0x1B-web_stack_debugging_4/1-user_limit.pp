# File: 1-user_limit.pp

# This manifest ensures that the 'holberton' user has increased limits for open file descriptors.

file_line { 'holberton_soft_nofile':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton soft nofile 4096',
  match  => '^holberton soft nofile',
}

file_line { 'holberton_hard_nofile':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton hard nofile 8192',
  match  => '^holberton hard nofile',
}
