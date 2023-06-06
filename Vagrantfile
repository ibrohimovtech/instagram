# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Box configuration
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20200304.0.0"

  # Port forwarding
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Provisioning
  config.vm.provision "shell", inline: <<-SHELL
    # Disable automatic package updates
    sudo systemctl disable apt-daily.service
    sudo systemctl disable apt-daily.timer

    # Update package manager and install necessary dependencies
    sudo apt-get update
    sudo apt-get install -y python3-venv python3-pip

    # Create a Python alias
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi

  SHELL
end
