#!/usr/bin/env python3

"""Main module for tf-pre-commit"""

# Import builtin python libraries
import argparse
import os
import subprocess
from collections.abc import Sequence

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"


def _option_parser(options_to_parse: str) -> list[str] | None:
    """
    Parse provided options and generate less error-prone options string
    :param options_to_parse: (str | LiteralString) Global options or options to parse
    :return: (str) parse options string
    """

    try:
        _options_without_double_quotes = options_to_parse.strip('"')
        _options_without_quotes = _options_without_double_quotes.strip("'")
        options = _options_without_quotes.split(" ")
        return options
    except Exception as err:
        print(f"Error: {err}: {options_to_parse}")


def fmt(global_options: str | None = None, options: str | None = None, target: str | bytes | None = None) -> int:
    """
    Run terraform linting
    :param global_options: Global options for terraform
    :param options: Options for terraform fmt command
    :param target: Target for terraform fmt command, can be directory or a file
    :return: status code of terraform linting
    """

    command = ["terraform"]
    if global_options is not None:
        global_options = _option_parser(options_to_parse=global_options)
        command.extend(global_options)
        command.append("fmt")
    else:
        command.append("fmt")
    if options is not None:
        options = _option_parser(options_to_parse=options)
        command.extend(options)
        command.append(target)
    else:
        command.append(target)

    try:
        response = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            check=True,
        )
        print(response.stdout, end="")
        print(f"Exit code: {response.returncode}")
        return response.returncode
    except subprocess.CalledProcessError as err:
        print(err.stdout, end="")
        print(f"Error Exit code for {target}: {err.returncode}")
        return err.returncode


def main(argv: Sequence[str] | None = None) -> int:
    """
    Main function for terraform fmt command

    :param argv: Command line arguments
    :return: exit code of terraform linting
    """

    parser = argparse.ArgumentParser(description="Run terraform linting")
    parser.add_argument("--global-options", help="Global options for terraform")
    parser.add_argument("--options", help="Options for terraform fmt")
    parser.add_argument("filenames", nargs="*", help="Filenames to run")
    args = parser.parse_args(argv)
    exit_code = 0
    if args.filenames:
        if args.options and "-recursive" in args.options:
            targets = {os.path.dirname(filename) for filename in args.filenames}
            set(targets)
            if "" in targets:
                targets.remove("")
                targets.add(".")
        else:
            targets = args.filenames
        for target in targets:
            if not target:
                return exit_code
            else:
                exit_code |= fmt(global_options=args.global_options, options=args.options, target=target)
        return exit_code
    else:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
