import re

log_line = "May 20 00:00:02 sshd[1235]: Failed password for invalid user admin from 10.0.0.2 port 22 ssh2"

pattern = re.compile(r"Failed password for invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)")
match = pattern.search(log_line)
print(match.groups() if match else "No match")
