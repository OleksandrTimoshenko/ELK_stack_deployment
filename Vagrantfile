Vagrant.configure("2") do |config|
  #vagrant plugin install vagrant-env
  config.env.enable
  #config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network "private_network", ip: "10.2.2.25"

  config.vm.define "server" do |machine|
    config.vm.provider "virtualbox" do |v|
      v.memory = 6048
      v.cpus = 4
    end
    machine.vm.box = 'ubuntu/bionic64'
    machine.vm.provision :ansible do |ansible|
      ansible.playbook = ENV["PLAYBOOK_NAME"]
      ansible.verbose = 'vv'
      ansible.extra_vars = {
        env_setup:             ENV["ENVIRONMENT"],
        aws_access_key:        ENV["AWS_ACCESS_KEY"],
        aws_secret_access_key: ENV["AWS_SECRET_ACCESS_KEY"],
        server_user:           "vagrant"
      }
    end
  end
end