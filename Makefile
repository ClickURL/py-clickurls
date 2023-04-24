help:
## The following commands can be used:
	@sed -n 's/^##//p' ${MAKEFILE_LIST}

env-up:
	docker-compose up -d --build

env-down:
	docker-compose down

env-clear:
	docker-compose down --remove-orphans -v --rmi=all

app:
	docker exec -it py-click-application bash

env-roll-migration:
## env-roll-migration: from env roll default migrations
	docker exec -it py-click-application make roll-migration

env-roll-back-migration:
## env-roll-back-migration:	from env roll back to base position
	docker exec -it py-click-application make roll-back-migration

roll-migration:
## roll-migration:	roll default migrations
	yoyo apply --batch

roll-back-migration:
## roll-back-migration:	roll back default migrations
	yoyo rollback --batch