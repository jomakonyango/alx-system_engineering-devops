# This Puppet manifest installs Flask version 2.1.0 and Werkzeug version 2.2.2 using pip3

package { 'python3-pip':
  ensure => present,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.2.2',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
