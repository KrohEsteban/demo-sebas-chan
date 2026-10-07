#!/usr/bin/env python3
"""Count lines, words and characters in text.

Text is read from a file, a command-line argument or standard input, in that
order of precedence, and the selected counts are printed.
"""

import argparse
import json
import sys

METRICS = ("lines", "words", "chars")
DEFAULT_ENCODING = "utf-8"
PROG = "textcount"


class NoInputError(Exception):
    """Raised when no input source is available."""


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Count lines, words and characters in text.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        default=None,
        help="Literal text to process.",
    )
    parser.add_argument(
        "--file",
        "-f",
        dest="file",
        default=None,
        help="Path to a UTF-8 file (takes precedence over the text argument).",
    )
    parser.add_argument(
        "--lines",
        action="store_true",
        help="Count lines.",
    )
    parser.add_argument(
        "--words",
        action="store_true",
        help="Count words.",
    )
    parser.add_argument(
        "--chars",
        action="store_true",
        help="Count characters.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the counts as a JSON object.",
    )
    return parser


def select_metrics(args: argparse.Namespace) -> list[str]:
    """Return the metrics selected on the command line, defaulting to all."""
    selected = [metric for metric in METRICS if getattr(args, metric)]
    return selected or list(METRICS)


def read_file(path: str) -> str:
    """Read a UTF-8 text file."""
    with open(path, encoding=DEFAULT_ENCODING) as handle:
        return handle.read()


def read_stdin() -> str:
    """Read all of standard input as UTF-8 text."""
    return sys.stdin.buffer.read().decode(DEFAULT_ENCODING)


def resolve_input(args: argparse.Namespace) -> str:
    """Resolve the text to process, honouring file > argument > stdin."""
    if args.file is not None:
        if args.text is not None:
            print(
                f"{PROG}: warning: text argument ignored because --file was given",
                file=sys.stderr,
            )
        return read_file(args.file)
    if args.text is not None:
        return args.text
    if sys.stdin.isatty():
        raise NoInputError("no input provided")
    return read_stdin()


def count_text(text: str) -> dict[str, int]:
    """Count lines, words and characters in text."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "chars": len(text),
    }


def main() -> int:
    """Run the text counter and return the process exit code."""
    parser = build_parser()
    args = parser.parse_args()
    try:
        text = resolve_input(args)
    except NoInputError as exc:
        print(f"{PROG}: error: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeDecodeError) as exc:
        print(f"{PROG}: error: {exc}", file=sys.stderr)
        return 1

    metrics = select_metrics(args)
    counts = count_text(text)
    selected = {metric: counts[metric] for metric in metrics}

    if args.json:
        print(json.dumps(selected))
    else:
        print(", ".join(f"{metric}: {selected[metric]}" for metric in metrics))
    return 0


if __name__ == "__main__":
    sys.exit(main())
