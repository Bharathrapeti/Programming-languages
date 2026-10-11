from datetime import datetime

try:
    data = open("report.txt").read()
    name = "report_backup_" + datetime.now().strftime("%Y-%m-%d") + ".txt"
    open(name, "w").write(data)
    print("Backup successful!")
except FileNotFoundError:
    print("Error: report.txt not found")
