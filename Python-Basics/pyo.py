import shutil
def backup_file():
    try:
        shutil.copy("report.txt","backup_report.txt")
        print("Backup successful!")
    except FileNotFoundError:
         print("Error:report.txt not found!")

backup_file()
                    
