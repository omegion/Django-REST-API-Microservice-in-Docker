start-dev:
	sudo docker-compose up

start-dev-daemon:
	sudo docker-compose up -d

stop-dev:
	# @eval sudo docker stop $$(sudo docker ps -a -q)
	sudo docker-compose down

start-prod:
	sudo docker-compose -f docker-compose.prod.yml up

ssh-web:
	sudo docker-compose exec web bash

build-prod:
	sudo docker-compose -f docker-compose.prod.yml build

build-dev:
	sudo docker-compose build