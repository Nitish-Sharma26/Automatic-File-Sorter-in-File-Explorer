import os, shutil

path = r"C:/Users/HP/OneDrive/Documents/dump/"

file_name = os.listdir(path)

folder_name = ['csv files', 'pdf files', 'word files']

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
        os.makedirs((path + folder_name[loop]))

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file )
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file )
    elif ".docx" in file and not os.path.exists(path + "word files/" + file):
        shutil.move(path + file, path + "word files/" + file )