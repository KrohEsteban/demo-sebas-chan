# demo-sebas-chan

Demo repository to practice a basic Git and GitHub workflow.

## Usage

Run the greeting script directly:

```sh
./hello.py
./hello.py --name Alice
```

Or through the Makefile:

```sh
make run
make run ARGS="--name Alice"
make check
```

## Text counting

`textcount.py` counts lines, words and characters. Input is read from a file, a
literal argument or stdin, in that order of precedence. Lines are `splitlines()`
segments, words are whitespace-separated tokens and characters are Unicode code
points (newlines are normalized to `\n` when reading files).

```sh
./textcount.py "hello world"
./textcount.py --file README.md --lines
printf 'a\nb\n' | ./textcount.py --words
./textcount.py "hello world" --json
```

Output defaults to all three metrics; select them with `--lines`, `--words` and
`--chars`. Pass `--json` for a flat object such as
`{"lines": 1, "words": 2, "chars": 11}`; selectors filter the JSON keys too.
When both `--file` and a literal text argument are given, the file wins and the
argument is ignored.

Through the Makefile:

```sh
make run-textcount ARGS='"hello world" --words'
```

`make check` validates Python syntax only; it does not exercise behaviour.
