deploy:
	fab prod deploy

addkey:
	eval `ssh-agent`
	ssh-add default.pem

provy:
	provy -s pre_setup

frontend:
	provy -s frontend
	
