import os 
import shutil 
import json 

# Directory Paths 

user = os.path.expanduser("~") 
downloads_path = f"{user}/Downloads" 
existingFiles = os.scandir(downloads_path) 

audio_path = f"{user}/Music" 
images_path = f"{user}/Pictures"
documents_path = f"{user}/Documents" 
virtual_machine_path = f"{user}/virtualmachines" 

directory_list = [downloads_path, audio_path, images_path, documents_path, virtual_machine_path] 

# Check if destination directories exist, create them if not. Then move files 

def moveFiles(file, destination): 
    print("[+] Checking if Destination Directories Exist") 
    try:
        for dir in directory_list:
            if os.path.exists(dir) == True: 
                print(f"{dir} exists") 
            else: 
                os.mkdir(dir) 
                print(f"Created directory at {dir}")
        shutil.move(file, destination)
    except shutil.Error as e:
        print(e)

# Map files to extensions and appropriate directory. 

def sortDownloads(downloads_path):
    with open("fileconfig.json", "r" ) as f: 
        file_types = json.load(f) 

    for file in file_types:
        destination = file["name"]


if __name__ == "__main__": 
    user = os.path.expanduser("~") 
    downloads_path = f"{user}/Downloads" 
    existingFiles = os.scandir(downloads_path) 

    sortDownloads(downloads_path) 
