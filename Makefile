.PHONY: run train test coverage docker-test

run:
	python run.py

train:
	python data/generate_synthetic_dataset.py
	python app/model/train_color_model.py

test:
	pytest tests/

coverage:
	coverage run -m pytest tests/
	coverage report
	coverage html

docker-test:
	docker build -t rubik-api .
	docker run --rm rubik-api pytest tests/
