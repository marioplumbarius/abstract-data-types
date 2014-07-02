$so_packages = ['tmux', 'curl', 'vim', 'ruby', 'rubygems']
$gems = ['gem install rspec-expectations', 'gem install rspec']
$apt_update = 'apt-get update'
$gem_install = 'gem install'
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

exec {
  $gems:
  path => $PATH,
  user => 'root',
  require => [Exec[$apt_update], Package[$so_packages]]
}