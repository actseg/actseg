init:
	pip install -e .[dev]
	pip install -r requirements-dev.txt

test:
	tox

build:
	python setup.py bdist_wheel sdist

clean:
	rm -r build/
	rm -r dist/

publish:
	pip install twine
	twine upload dist/*