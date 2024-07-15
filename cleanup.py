import os 
import logging 
import time 
from watchdog.observers import Observer 
from watchdog.events import LoggingEventHandler 

# File Types 

file_extensions = {
    'audio': [".mp3", ".wav"],
    'images': [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
    'document_types': [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    'virtual_machines': [".iso", ".img", ".vdi", ".vmdk", ".vhd", ".vdi"]
}

# Directory Paths 

user = os.path.expanduser("~") 

downloads_path = f"{user}/Downloads" 

audio_path = f"{user}/Music" 
images_path = f"{user}/Pictures"
documents_path = f"{user}/Documents" 
virtual_machine_path = f"{user}/virtualmachines" 

# Create Directories if They Don't Exist 

directory_list = [downloads_path, audio_path, images_path, documents_path, virtual_machine_path] 

print("[+] Checking if Destination Directories Exist") 

for dir in directory_list:
    if os.path.exists(dir) == True: 
        print(f"{dir} exists") 
    else: 
        os.mkdir(dir) 
        print(f"Created directory at {dir}")

# Scan Downloads Directory and Return List 

print("[+] Files Currently in Downloads") 

for file in os.scandir(downloads_path): 
    print(file.name) 

print("[+] Moving Files to Corresponding Directories")



