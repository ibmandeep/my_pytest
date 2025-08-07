# # Variables
# APP_NAME = my_app
# DB_NAME = $(APP_NAME)_development
# ENV ?= development
BRANCH ?= $(shell git branch --show-current)

# Default task
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make branch-new NAME=feature-x   # Create new branch"
	@echo "  make pull            # Pull latest changes from current branch"
	@echo "  make push MSG='msg'  # Add, commit, and push"
	@echo "  make status          # Show git status"


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
