import unittest
import os
import tempfile
from src import log_parser

#Class to test the log_parser module
class TestLogParser(unittest.TestCase):

    #Test extract_failed_logins function
    def test_extract_failed_logins(self):
        log_data = """May 20 00:00:01 sshd[1234]: Failed password for user root from 192.168.1.100 port 22 ssh2
May 20 00:00:02 sshd[1235]: Failed password for invalid user admin from 10.0.0.2 port 22 ssh2
May 20 00:00:03 sshd[1236]: Failed password for user root from 192.168.1.100 port 22 ssh2"""

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmpfile:
            tmpfile.write(log_data)
            tmpfile_path = tmpfile.name

        result = log_parser.extract_failed_logins(tmpfile_path)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[("192.168.1.100", "root")], 2)
        self.assertEqual(result[("10.0.0.2", "admin")], 1)

        os.remove(tmpfile_path)  

    
    #Test generate_report function
    def test_generate_report(self):
        events = {
            ("192.168.1.100", "root"): 6,
            ("10.0.0.2", "admin"): 2
        }

        output_path = "reports/test_report.txt"
        log_parser.generate_report(events, output_path, threshold=5)

        with open(output_path, "r") as f:
            content = f.read()
        
        self.assertIn("IP: 192.168.1.100 | User: root | Failed Attempts: 6", content)
        self.assertIn("ALERT", content)
        self.assertIn("IP: 10.0.0.2 | User: admin | Failed Attempts: 2", content)


    #Remove the test files after running the tests.
    def tearDown(self):
        files_to_remove = [
            "logs/temp_test.log",
            "reports/test_report.txt",
            "reports/test_report.json"
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)



if __name__ == "__main__":
    unittest.main()
