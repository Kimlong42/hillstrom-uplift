# justfile
default: lint test

lint:
    uv run ruff check .

test:
    uv run pytest

data:
    uv run python -c "from hillstrom_uplift.data import download; download()"