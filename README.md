
# Base Converter

A small, interactive base converter written in Python. It converts numbers between bases 2 through 36 using the digits 0-9 and letters A-Z (case-insensitive).

This repository contains a single script, `main.py`, which provides a CLI prompt for converting numbers from one base to another.

## Features

- Convert numbers between bases 2..36
- Uses digits `0-9` and letters `A-Z` for digits >= 10
- Simple interactive command-line interface

## Requirements

- Python 3.6+

## Usage

Run the script with Python and follow the interactive prompts:

```bash
python3 main.py
```

Example session:

```
Convert yo nums jit
what number do you want to convert: ff
what is your number's base? (2-36): 16
what is your target base? (2-36): 10
Calculating...
255
```

Another example (binary -> hex):

```
what number do you want to convert: 11111111
what is your number's base? (2-36): 2
what is your target base? (2-36): 16
Calculating...
FF
```

## Implementation notes

- `main.py` exposes two helper functions:
	- `to_decimal(num_str, og_base)` — converts a number string in base `og_base` to a Python integer (decimal).
	- `from_decimal(dec_num, tar_base)` — converts a Python integer to a string representation in base `tar_base`.
- The script uses the character set `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ` for digit values.
- Input is case-insensitive for letters.

## Limitations and edge cases

- The script does not currently validate input characters rigorously. If you enter a character that is not valid for the given base, the program will raise a `ValueError` (from `.index()` on the digit string).
- Only integer (non-negative) values are supported as input. There is no support for fractional bases or negative numbers.

## Suggestions / Improvements

- Add input validation with helpful error messages when invalid digits or base values are entered.
- Add support for negative numbers and fractional conversions.
- Provide a non-interactive CLI (flags/arguments) to convert in scripts or pipelines.

## Contributing

If you want to improve functionality, please open a PR with tests and a short description of the change.

## License

No license specified. Check the repository owner for licensing details.
