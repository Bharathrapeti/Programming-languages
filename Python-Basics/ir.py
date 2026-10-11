def clean_file():
    with open("report.txt","r")as file:
        lines = file.readlines()
    with open("report_cleaned.txt","w")as file:
        file.writelines([line for line in lines if line.strip()])
        print("file cleaned successfully!")

clean_file()
