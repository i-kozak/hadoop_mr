#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    columns = line.strip().split(',')
    if len(columns) == 2:
        iata_code, airline_name = columns
        if 'iata' not in iata_code.lower():
            print('{}\t{}'.format(iata_code, airline_name))

    elif len(columns) == 31:
        airline_code = columns[4]
        delay = columns[11]
        if delay.lstrip('-').isdigit():
            print('{}\t{}'.format(airline_code, delay))
