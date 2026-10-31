# Python - Bootstrapping pytest Test Suite

This project is ready to go in a [dev container](https://containers.dev/), so you
don't need Python (or pipenv) installed on your machine at all — the
[ghcr.io/tdd-workshops/devcontainer-python](https://ghcr.io/tdd-workshops/devcontainer-python)
image provides everything needed.

## Getting started

Pick whichever option is easiest for you:

1. **GitHub Codespaces** — on GitHub, click **Code → Create codespace on main**.
   To open another branch, first select it from the branch selector above the
   file list. Then click **Code → Codespaces** and choose
   `Create codespace on <branch>`. The codespace will contain that branch's code.

2. **VS Code** — install the [Dev Containers] extension, open this folder and
   run **Dev Containers: Reopen in Container**.

3. **Other dev container compatible tools** (Gitpod, Cursor, etc.) — open this
   repository; they pick up `.devcontainer/devcontainer.json` automatically.

The first time the container starts, `make install-dependencies` runs
automatically (via `postCreateCommand`). It creates a `.venv` virtual
environment in the workspace and installs the pinned packages from
`requirements.txt` into it. VS Code automatically picks up the workspace
`.venv` as the project interpreter, so IntelliSense, terminals and the Test
Explorer all use it without extra setup.

## Running the tests

From a terminal inside the dev container (`.venv` is activated automatically):

```shell
pytest
```

or:

```shell
make test
```

You should see something like this:

```shell
============================= test session starts ==============================
platform linux -- Python 3.12.7, pytest-9.2.0, pluggy-1.7.0
rootdir: /workspaces/tdd-lab-python-pytest
collected 1 item

test_sum.py .                                                            [100%]

============================== 1 passed in 0.02s ===============================
```

Run `make help` to see all available targets.

## Project layout

- `sum.py` — the code under test:

  ```python
  class Sum:
      def addition(self, a, b):
          return a + b
  ```

- `test_sum.py` — the test suite:

  ```python
  from sum import Sum


  class TestSum:
      def test_additions_are_additive(self):
          sum = Sum()
          assert sum.addition(1, 1) == 2, "expected two numbers to add up"
  ```

- `requirements.txt` — pinned dependencies, installed with
  `make install-dependencies`
- `Makefile` — common tasks (`make help`)
- `.devcontainer/devcontainer.json` — dev container configuration

## About pytest

Pytest is a fairly magic library that extends Python's built-in `assert` to
handle most types in a nice understandable way. For instance, if you ask it to
compare two lists it'll happily tell you which of the two lists contains a
differing item and where it is. For example:

```python
def test_failing_lists(self):
    assert [1] == [1, 2]
```

will give you the following output:

```shell
=================================== FAILURES ===================================
_________________________ TestSum.test_failing_lists _________________________

self = <test_sum.TestSum object at 0x10205c8d0>

    def test_failing_lists(self):
>       assert [1] == [1, 2]
E       assert [1] == [1, 2]
E         Right contains one more item: 2
E         Use -v to get more diff

test_sum.py:9: AssertionError
=========================== short test summary info ============================
FAILED test_sum.py::TestSum::test_failing_lists
========================= 1 failed, 1 passed in 0.06s =========================
```

## About dev containers

Dev containers standardise a project's development environment in a
`.devcontainer/devcontainer.json` file at the root of the repository. Any tool
that understands the [dev container spec](https://containers.dev/) — VS Code,
GitHub Codespaces, Gitpod, and others — will build or reuse the same container
image, so every participant in a workshop gets an identical setup. The old
pipenv/Gitpod-specific configuration has been replaced by this single,
portable definition.

[Dev Containers]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
