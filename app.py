from flask import Flask, render_template
import re
import webbrowser
import threading


#Simple Flask web application that generates a report from a log file.
app = Flask(__name__)

#This runs the script as a subprocess and passes the necessary arguments.
def generate_report():
    cmd = [
        "python3",
        "src/log_parser.py",
        "--log", "logs/sample_auth.log",
        "--output", "reports/example_report.txt",
        "--json", "reports/example_report.json",
        "--threshold", "5"
    ]
    try:
        subprocess.run(cmd, check=True)
        print("[INFO] Report generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to generate report: {e}")


#This function parses the report file and extracts relevant information.
def parse_report_file(report_path):
    entries = []
    pattern = re.compile(r"IP: (\d+\.\d+\.\d+\.\d+) \| User: (\w+) \| Failed Attempts: (\d+)(.*)")
    with open(report_path, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip, user, count, alert = match.groups()
                entries.append({
                    "ip": ip,
                    "user": user,
                    "failed_attempts": int(count),
                    "alert": "[ALERT]" in alert
                })
    return entries


#Index route to display the report.
@app.route("/")
def index():
    report_path = "reports/example_report.txt"
    data = parse_report_file(report_path)

    alert_entries = [e for e in data if e["alert"]]
    all_entries = data

    return render_template("report.html", alert_entries=alert_entries, all_entries=all_entries)


if __name__ == "__main__":
    threading.Timer(1.25, lambda: webbrowser.open("http://localhost:8080")).start()
    app.run(debug=True, host="0.0.0.0", port=8080)
