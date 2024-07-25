import os 
import shutil 
from pathlib import Path
import json 

# Check if destination directories exist, create them if not. Then move files 

def moveFiles(file, destination): 
    print(f"[+] Moving {file.name} to {destination}") 
    try:
        if not destination.exists(): 
            destination.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(destination))
    except shutil.Error as e:
        print(e)

# Map files to extensions and appropriate directory. 

def sortDownloads(downloads_path):
    with open("fileconfig.json", "r" ) as f: 
        file_types = json.load(f) 
        extension_map = {}

    for category in file_types:
        folder_type = category["name"]
        for extension in category["extensions"]:
           extension_map[extension] = folder_type
            
    for file in downloads_path.iterdir(): 
        if file.is_file() and not file.name.startswith("."):
            destination = extension_map.get(file.suffix, "Other") 
            moveFiles(file, Path(user).joinpath(destination)) 

if __name__ == "__main__": 
    user = str(Path.home()) 
    downloads_path = Path(f"{user}/Downloads") 

    sortDownloads(downloads_path) 
