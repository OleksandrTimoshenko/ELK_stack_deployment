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
         ENVIRONMENT=vagrant \
	     vagrant up --provision;"
    )

@task
def vagrant_destroy(c):
    system(
        "PLAYBOOK_NAME=install_elk.yaml \
	     vagrant destroy -f;"
    )