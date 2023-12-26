help:
	@echo ""
	@echo "make build .... build container"
	@echo "make deploy ... deploy app"
	@echo ""

build:
	@docker compose build
		
deploy:
	@ssh debris "cd container_host/homekit-logger && docker compose down || exit 0"
	@ssh debris "cd container_host/homekit-logger && git pull"
	@ssh debris "cd container_host/homekit-logger && docker compose up -d --build"
