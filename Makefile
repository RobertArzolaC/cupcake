ssh-django-dev:
	docker exec -ti django bash

docker-up-dev:
	docker-compose -f compose-dev.yml up

docker-build-dev:
	docker-compose -f compose-dev.yml build

restart-django-dev:
	docker restart cupcake_django_1

ssh-django:
	docker exec -ti cupcake_django_1 bash

stop-all-container:
	docker container stop $(shell docker container ls -aq)

ps:
	docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}"
