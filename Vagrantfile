# -*- mode: ruby -*-
# vi: set ft=ruby :

$script_1 = <<SCRIPT
sudo apt-get update
sudo apt-get install python -y
sudo apt-get install vim -y
sudo apt-get install tree -y
sudo apt-get install ruby gem -y
sudo apt-get install build-essential python-dev -y
sudo apt-get install mongodb -y
sudo apt-get install gfortran libopenblas-dev liblapack-dev -y
sudo apt-get install python-numpy python-scipy -y
sudo gem install json
mkdir collect_n_serve
mkdir collect_n_serve/tools
sudo chgrp vagrant collect_n_serve
sudo chown vagrant collect_n_serve
sudo chgrp vagrant collect_n_serve/tools
sudo chown vagrant collect_n_serve/tools
mkdir BeautifulSoup-3.2.1
sudo chgrp vagrant BeautifulSoup-3.2.1
sudo chown vagrant BeautifulSoup-3.2.1
sudo umount /vagrant
SCRIPT

$script_2 = <<SCRIPT
tar -xvf /home/vagrant/collect_n_serve/tools/BeautifulSoup-3.2.1.tar.gz -C /home/vagrant/collect_n_serve/tools/
tar -xvf /home/vagrant/collect_n_serve/tools/pymongo-2.7.2.tar.gz -C /home/vagrant/collect_n_serve/tools/
cd /home/vagrant/collect_n_serve/tools/BeautifulSoup-3.2.1
sudo python setup.py install
cd /home/vagrant/collect_n_serve/tools/pymongo-2.7.2
sudo python setup.py install
cd /home/vagrant
chmod g-wx,o-wx /home/vagrant/.python-eggs
SCRIPT

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "hashicorp/precise32"
  config.vm.provider "virtualbox" do |v|
    v.name = "bfs__page_crawler"
  end
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "file", source: "collect/page/page1.py", destination: "page.py"
  config.vm.provision "file", source: "collect/page/db/mongo/page_mongo.py", destination: "page_mongo.py"

  config.vm.provision "shell", inline: $script_1

  # copy beautifulsoup files to vm
  config.vm.provision "file", source: "tools/BeautifulSoup-3.2.1.tar.gz", destination: "~/collect_n_serve/tools/BeautifulSoup-3.2.1.tar.gz"
  config.vm.provision "file", source: "tools/pymongo-2.7.2.tar.gz", destination: "~/collect_n_serve/tools/pymongo-2.7.2.tar.gz"

  # install beautifulsoup
  config.vm.provision "shell", inline: $script_2
end
