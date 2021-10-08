init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt
test:
	pytest