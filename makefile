format:
	black main.py utils.py

lint:
	pylint main.py utils.py

test:
	pytest main.py