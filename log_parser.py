import argparse
import re
from collections import Counter


def count(file):
    ip_entries_count = Counter()
    keywords = {"WARN", "ERROR", "INFO"}
    log_entries_count = Counter()
    process_entries_count = Counter()
    for line in file:
        clean = line.split()
        if len(clean) < 4:
            continue
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        if ip:
            ip_entries_count.update(ip)
            process_entries_count.update([clean[4]])
        else:
            if clean[2] in keywords:
                process_entries_count.update([clean[3]])
        matching_lines = [word for word in clean if word in keywords]
        log_entries_count.update(matching_lines)
    return ip_entries_count, process_entries_count, log_entries_count


def print_summary(log_count, process_count, ip_count):
    if log_count:
        top_log, log_occurrences = log_count.most_common(1)[0]
        print(f"'{top_log}' was the most common log type ({log_occurrences} occurrences).")
    else:
        print("No log keywords found.")

    if ip_count:
        top_ip, ip_occurrences = ip_count.most_common(1)[0]
        print(f"'{top_ip}' was the most common IP address ({ip_occurrences} occurrences).")
    else:
        print("No IP addresses and processes found.")

    if process_count:
        top_process, process_occurrences = process_count.most_common(1)[0]
        print(f"'{top_process}' was the most common process ({process_occurrences} occurrences).")


def log_parse(f):
    try:
        with open(f, 'r') as file:
            ip_count, process_count, log_count = count(file)
            print_summary(log_count, process_count, ip_count)
    except FileNotFoundError:
        print("File is not found")
        return


def main():
    parser = argparse.ArgumentParser(description="A script that processes a given file.")
    parser.add_argument("filename", help="The path to the file you want to process")
    args = parser.parse_args()
    target_file = args.filename
    log_parse(target_file)


if __name__ == "__main__":
    main()
