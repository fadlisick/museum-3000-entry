# Museum of the Year 3000

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

A make.fun entry for **Museum of the Year 3000**: one deadpan museum label
from the year 3000, placed beside an ordinary object from today.

## The label

> Lint roller, c. 2023. A ceremonial adhesive wand, rolled over clothing to
> remove the sins of pet ownership.

The year 3000 misreads the lint roller as a ceremonial adhesive wand: it
really does roll over clothing to take away the traces of pet ownership, and
the label says so with a straight face.

## How it works

`main.py` deterministically writes the label to `/output/entry.txt`
(107 characters, single line, no em dash), sets mode 0644, and verifies the
file byte-for-byte against the locked label plus a gate self-check
(1 to 200 characters).

```sh
python3 main.py
```
