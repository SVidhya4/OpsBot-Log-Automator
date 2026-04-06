import os
import re
import time
from datetime import datetime

class OpsBot:
    def __init__(self, log_file):
        self.log_file = log_file
        self.targets = ["CRITICAL", "ERROR", "FAILED LOGIN"]
        self.lower_targets = [t.lower() for t in self.targets]
        self.stats = {key: 0 for key in self.targets}

    def analyze(self, chunk_size=1024 * 1024):
        """Reads logs in 1MB chunks to stay memory-efficient."""
        if not os.path.exists(self.log_file):
            print(f"Error: {self.log_file} not found.")
            return

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_name = f"security_alert_{report_date}.txt"

        with open(self.log_file, 'r') as f, open(report_name, 'w') as report:
            report.write(f"--- OpsBot Security Report ({report_date}) ---\n")
            report.write("="*45 + "\n\nDetailed Alert Logs:\n")
            report.write("="*45 + "\n")
            
            while True:
                lines = f.readlines(chunk_size)
                if not lines:
                    break
                
                for line in lines:
                    self.process_line(line, report)
        
        self.append_summary(report_name)

    def process_line(self, line, report):
        """Standardizes case and checks for target keywords."""
        is_alert = False
        lower_line = line.lower()
        
        for i, t_lower in enumerate(self.lower_targets):
            if t_lower in lower_line:
                self.stats[self.targets[i]] += 1
                is_alert = True
        
        if is_alert:
            report.write(line)

    def append_summary(self, report_name):
        """Adds the final counts to the bottom of the report."""
        with open(report_name, 'a') as f:
            f.write("\n" + "="*45 + "\n")
            f.write("SUMMARY STATISTICS\n")
            f.write("="*45 + "\n")
            for target, count in self.stats.items():
                f.write(f"{target}: {count}\n")
        
        size = os.path.getsize(report_name)
        print(f"Report Ready: {report_name} ({size:,} bytes generated).")

if __name__ == "__main__":
    bot = OpsBot("server.log")
    start = time.time()
    bot.analyze()
    print(f"Analysis Time: {time.time() - start:.2f} seconds.")
