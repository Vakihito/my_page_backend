run:
	poetry run uvicorn src.main.main:app --reload

check-black:
	poetry run black src tests --line-length 120 --check

fix-black:
	poetry run black src --line-length 120

# creates a new migration based on the model changes pass the name as a parameter
# Ex: make migrate-auto name="create_feedback_table"
migrate-auto:
	poetry run alembic revision --autogenerate -m "$(name)"

# updates with the lastest migrations
migrate-up:
	poetry run alembic upgrade head

# resets the migration
# Ex: make migrate-reset version=d5a0c49799af
migrate-down:
	poetry run alembic downgrade $(version)

# create a template for a new route in application backent
# main - refer to the name of the main subfolder - such as 'goals'
# service - refer to the specific service that we are creating - like 'update'
# Ex: make route main='goals' service='update'
route:
	poetry run black src --line-length 120 && \
	python utils/make_route.py $(main) $(service) && \
	poetry run black src --line-length 120 