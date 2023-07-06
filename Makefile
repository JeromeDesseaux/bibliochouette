COMPOSE=docker compose --env-file .env -f docker/docker-compose.yml

start-dev:
	${COMPOSE} up --force-recreate --build --no-deps

bash:
	docker exec -it bibliochouette_api /bin/bash

createsuperuser:
	python manage.py createsuperuser --no-input

config:
	${COMPOSE} config

purge:
	${COMPOSE} down
	docker rm -f $(docker ps -aq) && docker volume rm $(docker volume ls -q)
