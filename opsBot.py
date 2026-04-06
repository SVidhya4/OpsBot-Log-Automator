import os
import re
import time
from datetime import datetime

class OpsBot:
    def __init__(self, log_file):
        self.log_file = log_file
        self.targets = ["CRITICAL", "ERROR", "FAILED LOGIN"]
        self.stats = {key: 0 for key in self.targets}
        self.alerts = []

    def analyze(self, chunk_size=1024 * 1024):
        """Reads logs in 1MB chunks to stay memory-efficient."""
        if not os.path.exists(self.log_file):
            print(f"Error: {self.log_file} not found.")
            return

        with open(self.log_file, 'r') as f:
            while True:
                lines = f.readlines(chunk_size)
                if not lines:
                    break
                
                for line in lines:
                    self.check_line(line)
        
        self.generate_report()

    def check_line(self, line):
        """Standardizes case and checks for target keywords."""
        is_alert = False
        lower_line = line.lower()
        
        for target in self.targets:
            if target.lower() in lower_line:
                self.stats[target] += 1
                is_alert = True
        
        if is_alert:
            self.alerts.append(line.strip())

    def generate_report(self):
        """Generates the required security_alert_[date].txt file."""
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_name = f"security_alert_{report_date}.txt"
        
        with open(report_name, "w") as f:
            f.write(f"--- OpsBot Security Report ({report_date}) ---\n")
            f.write("="*45 + "\n\n")
            
            f.write("Summary Statistics:\n")
            for target, count in self.stats.items():
                f.write(f"- {target}: {count}\n")
            
            f.write("\n" + "="*45 + "\n")
            f.write("Filtered Alert Logs:\n")
            f.write("="*45 + "\n")
            
            for alert in self.alerts:
                f.write(alert + "\n")
        
        if os.path.exists(report_name):
            size = os.path.getsize(report_name)
            print(f"Report Ready: {report_name} ({size:,} bytes generated).")

if __name__ == "__main__":
    bot = OpsBot("server.log")
    start = time.time()
    bot.analyze()
    print(f"Analysis Time: {time.time() - start:.2f} seconds.")