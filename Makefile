build:
	docker-compose -f docker-compose.yml build
run:
	docker-compose -f docker-compose.yml up -d
down:
	docker-compose -f docker-compose.yml down
restart:
	docker-compose -f docker-compose.yml restart main-service
logs:
	docker-compose -f docker-compose.yml logs --tail=50 -f main-service
exec:
	docker-compose -f docker-compose.yml exec main-service /bin/bash