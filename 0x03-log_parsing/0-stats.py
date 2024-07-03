#!/usr/bin/python3
"""
Working for the interview
"""
import sys
import signal


total_size = 0
status_counts = {}
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0


def print_stats():
    """
    Get the print stats
    """
    global total_size, status_counts
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line):
    """
    Get the process line
    """
    global total_size, status_counts, valid_status_codes
    parts = line.split()
    if len(parts) < 7:
        return
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        if status_code in valid_status_codes:
            total_size += file_size
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1
    except (ValueError, IndexError):
        return


def signal_handler(sig, frame):
    """
    Returns the signal
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    process_line(line.strip())
    line_count += 1
    if line_count % 10 == 0:
        print_stats()

# Final stats output
print_stats()
