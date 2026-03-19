install:
	uv sync

brain-games:
	uv run brain-games

brain-calc:
	uv run brain-calc

brain-progression:
	uv run brain-progression

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