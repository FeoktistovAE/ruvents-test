setup: install build package-install

install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
help:
	poetry run test_task -h