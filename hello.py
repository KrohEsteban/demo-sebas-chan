#!/usr/bin/env python3
"""Minimal greeting command-line script."""

import argparse

DEFAULT_NAME = "World"


def main() -> None:
    """Print a greeting, optionally personalised with --name."""
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument(
        "--name",
        default=DEFAULT_NAME,
        help="Name to greet (default: %(default)s).",
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
