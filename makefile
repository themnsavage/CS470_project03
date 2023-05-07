APP_NAME = cs470_project

build:
	docker build -t $(APP_NAME) .
run:
	docker run -i -t $(APP_NAME) python3 main.py
analyze:
	docker run -i -t $(APP_NAME) python3 analyze.py

reduction:
	docker run -t $(APP_NAME) python3 reduction.py

generate:
	docker run -t $(APP_NAME) python3 generate.py

clean:
	docker rmi -f $(APP_NAME)