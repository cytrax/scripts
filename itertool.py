#!/usr/local/bin/python3
from itertools import count
sequence = filter(
	lambda square: square % 3 == 0 and square % 2 == 1,
	map(lambda number = number ** 2, count ())
	)

