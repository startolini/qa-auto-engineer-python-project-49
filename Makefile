install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl