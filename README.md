# tf-pre-commit

Python base simple terraform pre-commit hook.

## Python Version

Requires `python` version `3.9` or above.

## Table of Contents

- [Using tf-pre-commit with pre-commit](#using-tf-pre-commit-with-pre-commit)
- [Development](#development)
- [License](#license)

## Using `tf-pre-commit` with `pre-commit`

Add the following `repo` to your `.pre-commit-config.yaml`

```yaml
...
  - repo: https://github.com/devopsforhuman/tf-pre-commit
    rev: v1.0.1
    hooks:
      id: terraform-fmt
...
```
if you want to provide `options` or `global options` (try `terraform fmt --help`) then use `args`

```yaml
...
  - repo: https://github.com/devopsforhuman/tf-pre-commit
    rev: v1.0.1
    hooks:
      id: terraform-fmt
      args:
          - --options="-no-color -diff -check"
...
```

> **Note**
> If `-recursive` is provided in the `--options` argument, terraform formatting will recursively format the parent
> directory of the file in context.

## Development

- Create virtual environment

  ```shell
  python3 -m venv .venv
  ```

- Activate virtual environment

  ```shell
  source .venv/bin/activate
  ```

  or for windows

  ```shell
  .\.venv\Scripts\activate.ps1
  ```

- Install dependencies

  To install dependencies with `pipenv` use the following command

  ```shell
  python3 -m pip install -r requirements.txt
  ```

  To install `dev` dependencies use `--dev` flag

  ```shell
  python3 -m pip install -r requirements_dev.txt
  ```

## License

`tf-pre-commit` is distributed under the terms of the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license.
