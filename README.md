# Syslog Investigator

## Overview:

Lightweight Python-based tool designed to parse and analyze Linux system authentication logs. Its primary objective is to assist cybersecurity analysts and SOC professionals in detecting suspicious activities such as brute-force attacks and unauthorized login attempts.

## Key Features:

  - Extracts failed login attempts from system logs;
  - Aggregates source IPs and usernames involved in repeated failures;
  - Generates a concise summary report for further investigation.

## Technologies:

  - Python 3.x;
  - Regular Expressions;
  - File I/O.

## Project Structure:

  - `src/` – contains the log parsing script;
  - `logs/` – sample log files for testing;
  - `reports/` – generated analysis reports.

## Requirements:

All dependencies are listed in `requirements.txt`. This project uses only standard Python libraries.

## Getting Started:

```bash
python3 src/log_parser.py --log logs/sample_auth.log --output reports/example_report.txt
