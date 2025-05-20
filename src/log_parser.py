#!/usr/bin/env python3
import argparse
import re
import json
import logging


#Parsing Linux authentication logs to extract suspicious events.
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Parse Linux authentication logs and extract suspicious events."
    )
    parser.add_argument("--log", required=True, help="Path to the syslog file")
    parser.add_argument("--output", required=True, help="Path to save the TXT report")
    parser.add_argument("--threshold", type=int, default=5,
                        help="Threshold for failed attempts to trigger an alert (default: 5)")
    parser.add_argument("--json", help="Optional path to save the report in JSON format")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose debug output")
    return parser.parse_args()


#Extracting failed login attempts from the syslog file.
def extract_failed_logins(log_path):
    pattern_invalid = re.compile(r"Failed password for invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)")
    pattern_valid = re.compile(r"Failed password for user (\w+) from (\d+\.\d+\.\d+\.\d+)")

    events = {}

    with open(log_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            match_invalid = pattern_invalid.search(line)
            match_valid = pattern_valid.search(line)

            if match_invalid:
                user, ip = match_invalid.groups()
                logging.debug(f"[Line {line_number}] Failed login for INVALID user '{user}' from {ip}")
            elif match_valid:
                user, ip = match_valid.groups()
                logging.debug(f"[Line {line_number}] Failed login for user '{user}' from {ip}")
            else:
                logging.debug(f"[Line {line_number}] No match.")
                continue

            key = (ip, user)
            events[key] = events.get(key, 0) + 1

    return events


#Generating a report of suspicious authentication failures.
def generate_report(events, output_path, threshold):
    with open(output_path, "w") as report:
        report.write("Suspicious Authentication Failures Report:\n")
        report.write("=" * 50 + "\n\n")
        for (ip, user), count in sorted(events.items(), key=lambda x: x[1], reverse=True):
            alert = " ------------------------> [ALERT]" if count >= threshold else ""
            report.write(f"IP: {ip} | User: {user} | Failed Attempts: {count}{alert}\n")


#Generating a JSON report of suspicious authentication failures.
def generate_json(events, json_path, threshold):
    data = []

    for (ip, user), count in sorted(events.items(), key=lambda x: x[1], reverse=True):
        data.append({
            "ip": ip,
            "user": user,
            "failed_attempts": count,
            "alert": count >= threshold
        })

    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


#Main function to parse arguments and generate reports.
def main():
    args = parse_arguments()

    logging_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info(f"Parsing log file: {args.log}")
    events = extract_failed_logins(args.log)
    logging.info(f"Total suspicious events found: {len(events)}")

    generate_report(events, args.output, args.threshold)
    logging.info(f"TXT report generated: {args.output}")

    if args.json:
        generate_json(events, args.json, args.threshold)
        logging.info(f"JSON report generated: {args.json}")


#This script is designed to be run from the command line.
if __name__ == "__main__":
    main()
