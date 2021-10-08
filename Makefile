init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt

test:
	pytest

build:
	python setup.py bdist_wheel sdist

clean:
	rm -r build/
	rm -r dist/

publish:
	pip install twine>=3.4.2
	twine upload dist/*