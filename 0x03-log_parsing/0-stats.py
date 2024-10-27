#!/usr/bin/python3
"""
Script to parse and display log statistics
"""

import sys
import re


def display_log_stats(stats: dict) -> None:
    """
    Display the file size and status code frequencies
    """
    print("File size: {}".format(stats["file_size"]))
    for status_code in sorted(stats["code_counts"]):
        if stats["code_counts"][status_code]:
            print("{}: {}".format(status_code, stats["code_counts"][status_code]))


if __name__ == "__main__":
    log_pattern = re.compile(
        r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  # noqa: E501
    )

    line_total = 0
    stats = {"file_size": 0, "code_counts": {str(code): 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}}

    try:
        for input_line in sys.stdin:
            input_line = input_line.strip()
            log_match = log_pattern.fullmatch(input_line)
            if log_match:
                line_total += 1
                status_code = log_match.group(2)
                size = int(log_match.group(3))

                # Update file size
                stats["file_size"] += size

                # Update status code count
                if status_code in stats["code_counts"]:
                    stats["code_counts"][status_code] += 1

                if line_total % 10 == 0:
                    display_log_stats(stats)
    finally:
        display_log_stats(stats)
