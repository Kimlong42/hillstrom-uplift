# justfile
default: lint test

lint:
    uv run ruff check .
    uv run ruff format --check .

fmt:
    uv run ruff check --fix .
    uv run ruff format .

test:
    uv run pytest

data:
    uv run python -c "from hillstrom_uplift.data import download; download()"