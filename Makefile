## Build api docker containers
docker_build:
	docker-compose up --build -d

## Migrate database
migrate:
	poetry run python -m scripts.migrate

## Rollback migrations in database
migrate-rollback:
	poetry run python -m scripts.migrate --rollback

migrate-reload:
	poetry run python -m scripts.migrate --reload
