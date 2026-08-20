format:
	python3 -m black .
	python3 -m isort .

lint:
	python -m pylint energy_insights

run:
	python -m energy_insights --help