#!/usr/bin/python3
"""
This script reads log data from standard input
line by line and computes statistics.
"""
import sys

status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
}

file_size = 0


def print_stats():
    """Prints statistics based on the logs."""
    print("File size:", file_size)
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))


if __name__ == "__main__":
    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            try:
                elem = line.split()
                file_size += int(elem[-1])
                if elem[-2] in status_codes:
                    status_codes[elem[-2]] += 1
            except Exception:
                pass
            if line_number % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
