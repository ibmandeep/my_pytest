# # Variables
# APP_NAME = my_app
# DB_NAME = $(APP_NAME)_development
# ENV ?= development
BRANCH ?= $(shell git branch --show-current)

# Default task
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make setup           # Install gems, setup DB"
	@echo "  make db              # Create, migrate, seed DB"
	@echo "  make migrate         # Run DB migrations"
	@echo "  make seed            # Seed the DB"
	@echo "  make test            # Run test suite"
	@echo "  make server          # Start Rails server"
	@echo "  make console         # Open Rails console"
	@echo "  make clean           # Clean logs and temp files"
	@echo "  make reset           # Drop and recreate DB"
	@echo "  make branch-new NAME=feature-x   # Create new branch"
	@echo "  make pull            # Pull latest changes from current branch"
	@echo "  make push MSG='msg'  # Add, commit, and push"
	@echo "  make status          # Show git status"

### Rails Commands

setup:
	bundle install
	bin/rails db:setup

db:
	bin/rails db:create db:migrate db:seed

migrate:
	bin/rails db:migrate

seed:
	bin/rails db:seed

test:
	bin/rails test

server:
	bin/rails server -b 0.0.0.0

console:
	bin/rails console

clean:
	rm -rf tmp/*
	rm -f log/*.log

reset:
	bin/rails db:drop db:create db:migrate db:seed

### Git Commands

branch-new:
	git checkout -b $(NAME)

pull:
	git pull origin $(BRANCH)

push:
	git add .
	git commit -m "$(MSG)"
	git push origin $(BRANCH)

status:
	git status
