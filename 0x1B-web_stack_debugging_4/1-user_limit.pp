# File: 1-user_limit.pp

# This manifest increases the limit on the number of open file descriptors for the 'holberton' user.

exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/echo "holberton soft nofile 4096" >> /etc/security/limits.conf \
              && /bin/echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  unless  => '/bin/grep -q "holberton soft nofile" /etc/security/limits.conf',
}
