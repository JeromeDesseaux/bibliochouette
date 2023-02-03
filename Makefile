start-dev:
	docker compose -f docker/docker-compose.yml up --force-recreate --build --no-deps

createsuperuser:
	python manage.py createsuperuser --no-input