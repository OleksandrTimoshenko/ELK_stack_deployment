Vagrant.configure("2") do |config|
  #vagrant plugin install vagrant-env
  config.env.enable
  #config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network "private_network", ip: "10.2.2.25"

  config.vm.define "server" do |machine|
    config.vm.provider "virtualbox" do |v|
      v.memory = 4048
      v.cpus = 4
    end
    machine.vm.box = 'ubuntu/bionic64'
    machine.vm.provision :ansible do |ansible|
      ansible.playbook = ENV["PLAYBOOK_NAME"]
      ansible.verbose = 'vv'
      ansible.extra_vars = {
        env_setup: ENV["ENVIRONMENT"]
    #    gitlab_user: ENV["REGISTRY_USER"],
    #    gitlab_token: ENV["REGISTRY_TOKEN"],
    #    postgres_user: ENV["POSTGRES_USER"],
    #    postgres_db: ENV["POSTGRES_DB"],
    #    backup_name: ENV["BACKUP_NAME"],
    #    current_env: ENV["CURRENT_ENV"]
      }
    end
  end
end