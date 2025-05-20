# Syslog Investigator

## Overview:

Lightweight Python-based tool designed to parse and analyze Linux system authentication logs. Its primary objective is to assist cybersecurity analysts and SOC professionals in detecting suspicious activities such unauthorized login attempts.


## Key Features:

  - Extracts failed login attempts from system logs;
  - Aggregates source IPs and usernames involved in repeated failures;
  - Generates detailed reports in both text and JSON formats;
  - Provides a web dashboard to visualize all entries and alerts.


## Technologies:

  - Python 3.x;
  - Flask Web Framework;
  - Regex;
  - JSON;
  - HTML.


## Project Structure:

```plaintext syslog-investigator/ ├── app.py # Flask application and report visualization ├── src/ │ └── log_parser.py # Log parsing and report generation script ├── logs/ │ └── sample_auth.log # Sample SSH authentication log file ├── reports/ │ ├── example_report.txt # Generated textual report │ └── example_report.json # Generated JSON report ├── templates/ │ ├── report.html # Main dashboard HTML template │ └── index.html # Optional landing page template ├── tests/ │ └── test_log_parser.py # Unit tests for log parsing ├── requirements.txt # Python dependencies └── README.md # Project documentation ``` 


## Intallation:
1. Clone the repository:
```text
git clone https://github.com/lucasferrao/syslog-investigator.git
```
```bash
cd syslog-investigator
```
    
2. Create and activate a virtual environment:
   - python3 -m venv venv
   - source venv/bin/activate        # Linux/macOS
   - venv\Scripts\activate.bat       # Windows

3. Install required packages:
```python
pip install -r requirements.txt
```

5. Run the application:
```python
python app.py
```

## Web Dashboard
  - Alerts Table: Lists all IP/user entries with failed attempts exceeding the alert threshold;
  - All Entries Table: Displays every parsed failed login attempt with details;
  - This interface enables cybersecurity analysts to quickly identify and investigate suspicious authentication activity.


## Testing
```python
python -m unittest discover tests
```


## License
  - [MIT](https://choosealicense.com/licenses/mit/)


## Authors
- [@lucasferrao](https://www.github.com/lucasferrao)


## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucaslfferrao)
