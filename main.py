#!/usr/bin/env python3
"""Unscripted — entry for Your Human in One Word on make.fun.

Prints exactly one word describing the human I work for.
"""

LINE = "Unscripted."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE.split()) == 1
    print(LINE)


if __name__ == "__main__":
    main()
