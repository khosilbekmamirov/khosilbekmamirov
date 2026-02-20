import re
from collections import Counter
import argparse

def parse_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    ips = []
    for line in lines:
        match = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ips.append(match.group(1))
    return Counter(ips)

def main():
    parser = argparse.ArgumentParser(description='Simple log intrusion detector')
    parser.add_argument('logfile', help='Path to log file')
    args = parser.parse_args()

    ip_counts = parse_log(args.logfile)
    print("Top suspicious IPs:")
    for ip, count in ip_counts.most_common(5):
        print(f"{ip} - {count} failed attempts")

if __name__ == "__main__":
    main()
