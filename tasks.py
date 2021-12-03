from invoke import task
from dotenv import load_dotenv
from os import system

load_dotenv()

# run for the first time only
@task
def install_vagrant_plugins(c):
    c.run("vagrant plugin install vagrant-env")

@task
def vagrant_provision(c):
    system(
        "PLAYBOOK_NAME=install_elk.yaml \
         AWS_ACCESS_KEY=$AWS_ACCESS_KEY \
         AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
         ENVIRONMENT=vagrant \
	     vagrant up --provision;"
    )

@task
def vagrant_destroy(c):
    system(
        "PLAYBOOK_NAME=install_elk.yaml \
	     vagrant destroy -f;"
    )

@task()
def deploy_server(c):
    system(
        "ansible-playbook -v -i $SERVER_IP, --user $SSH_USER --private-key $KEY_RSA install_elk.yaml \
         --extra-vars \"server_user=$SERVER_USER \
                        aws_access_key=$AWS_ACCESS_KEY\
                        aws_secret_access_key=$AWS_SECRET_ACCESS_KEY \
                        domain_name=$DOMAIN_NAME \
                        email=$EMAIL \
                        env_setup=stage\""
    )

@task
def ssh_to_server(c):
    system("ssh -i $KEY_RSA $SSH_USER@$SERVER_IP")