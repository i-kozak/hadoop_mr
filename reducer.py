#!/usr/bin/env python
"""reducer.py"""

import sys

last_iata = ''
last_delay = []
last_name = ''
airline_avg_delay = {}

for line in sys.stdin:
    try:

        iata, value = line.strip().split('\t', 1)

    except ValueError:
        continue

    if iata == last_iata:
        try:

            last_delay.append(int(value))

        except ValueError:
            last_name = value
    else:
        if last_name and last_delay:
            airline_avg_delay['{}\t{}'.format(last_iata, last_name)] = float(sum(last_delay))/len(last_delay)
        last_iata = iata
        last_delay = []
        last_name = ''
        try:

            last_delay, last_name = [int(value)], ''

        except ValueError:
            last_delay, last_name = [], value

if last_name and last_delay:
    airline_avg_delay['{}\t{}'.format(last_iata, last_name)] = float(sum(last_delay))/len(last_delay)

for airline, delay in sorted(airline_avg_delay.items(), key=lambda kv: kv[1], reverse=True)[:5]:
    print('{}\t{}'.format(airline, delay))
