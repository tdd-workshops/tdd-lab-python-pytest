# Python pytest - Gilded Rose Refactoring Kata

This repository contains the Python version of Emily Bache's
[Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata),
using pytest.

Read [the requirements](GildedRoseRequirements.md), add tests to characterize the
existing behavior, then refactor `GildedRose.update_quality()` and add support for
Conjured items. Do not alter the `Item` class or the `items` property.

## Getting started

This project is ready to go in a [dev container](https://containers.dev/), so you
don't need Python installed on your machine. Pick whichever option is easiest
for you:

1. **GitHub Codespaces** — on GitHub, click **Code → Create codespace on main**.
   To open another branch, first select it from the branch selector above the
   file list. Then click **Code → Codespaces** and choose
   `Create codespace on <branch>`. The codespace will contain that branch's code.
2. **VS Code** — install the [Dev Containers] extension, open this folder and
   run **Dev Containers: Reopen in Container**.
3. **Other dev container compatible tools** (Gitpod, Cursor, etc.) — open this
   repository; they pick up `.devcontainer/devcontainer.json` automatically.

The first time the container starts, `make install-dependencies` creates a
workspace `.venv` and installs the pinned packages from `requirements.txt`.
VS Code uses this environment for IntelliSense, terminals and the Test Explorer.

## Running the tests

From a terminal inside the dev container:

```shell
pytest
```

or:

```shell
make test
```

Run `make help` to see all available targets.

## Project layout

- `gilded_rose.py` — the legacy `GildedRose` code and the `Item` model
- `test_gilded_rose.py` — the starting pytest test
- `test_gilded_rose_characterisation.py` — the 30-day golden-master test
- `texttests/ThirtyDays/stdout.gr` — the expected characterisation test output
- `GildedRoseRequirements.md` — the kata requirements
- `requirements.txt` — pinned Python dependencies
- `Makefile` — dependency installation and test tasks
- `.devcontainer/devcontainer.json` — dev container configuration

[Dev Containers]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
