$so_packages = ['python-pip', 'tmux', 'curl', 'vim']
$pip_packages = ['pip install ivoire', 'pip install expects']
$apt_update = 'apt-get update'
$PATH = '/usr/bin:/usr/sbin'

# update apt-get packages
exec {
  $apt_update:
  path => $PATH,
  user => 'root'
}

# install dependencies
package {
  $so_packages:
  ensure  => installed,
  require => Exec[$apt_update]
}

# install app dependencies
exec {
  $pip_packages:
  path => $PATH,
  user => 'root',
  require => [Exec[$apt_update], Package[$so_packages]]
}

# services
# service {
#   $services:
#   ensure  => running,
#   require => [Exec[$apt_update, $pip_packages], Package[$so_packages]]
# }

# include module_name