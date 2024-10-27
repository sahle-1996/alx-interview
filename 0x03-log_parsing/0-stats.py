#!/usr/bin/python3

"""
Script reads input line-by-line and computes log metrics.
"""

import sys

line_total = 0
file_size_sum = 0

code_counts = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
}

try:
    for input_line in sys.stdin:
        fields = input_line.split(' ')

        if len(fields) > 2:
            code = fields[-2]
            size = fields[-1]

            if code in code_counts:
                code_counts[code] += 1
            file_size_sum += int(size)
            line_total += 1

            if line_total == 10:
                print('File size: {:d}'.format(file_size_sum))
                for key in sorted(code_counts):
                    if code_counts[key] > 0:
                        print('{}: {}'.format(key, code_counts[key]))
                line_total = 0

except KeyboardInterrupt:
    print("\nUser interruption detected.")

finally:
    print("File size: {:d}".format(file_size_sum))
    for key in sorted(code_counts):
        if code_counts[key] > 0:
            print("{}: {}".format(key, code_counts[key]))
