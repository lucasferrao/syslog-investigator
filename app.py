from flask import Flask, render_template
import re

app = Flask(__name__)

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

@app.route("/")
def index():
    report_path = "reports/example_report.txt"
    data = parse_report_file(report_path)

    alert_entries = [e for e in data if e["alert"]]
    all_entries = data

    return render_template("report.html", alert_entries=alert_entries, all_entries=all_entries)

@app.route("/detailed")
def detailed():
    log_path = "logs/sample_auth.log"
    detailed_entries = extract_failed_logins_detailed(log_path)
    return render_template("detailed.html", entries=detailed_entries)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
