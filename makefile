start-dev:
	sudo docker-compose up

start-prod:
	sudo docker-compose -f docker-compose.prod.yml up

stop-compose:
	@eval docker stop $$(docker ps -a -q)
	sudo docker-compose down

ssh-web:
	sudo docker-compose exec web bash

build-prod:
	sudo docker-compose -f docker-compose.prod.yml build

build-dev:
	sudo docker-compose build