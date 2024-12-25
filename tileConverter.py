import os
import shutil
from pathlib import Path

def convert_tiles(source_dir, destination_dir):
    """
    Convert tile structure from {z}/{x}/{y}.jpg format to OSM format
    Correct format: osm_100-l-3-z-x-y.png
    """
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.jpg'):
                # Get the relative path components
                rel_path = os.path.relpath(root, source_dir)
                z, x = rel_path.split(os.sep)
                y = file.split('.')[0]
                
                # Convert to integer for validation
                z, x, y = int(z), int(x), int(y)
                
                # Create new filename in OSM format
                # Using format: osm_100-l-3-z-x-y.png
                new_filename = f"osm_100-l-3-{z}-{x}-{y}.png"
                
                # Create source and destination paths
                source_file = os.path.join(root, file)
                dest_file = os.path.join(destination_dir, "offline_tiles", new_filename)
                
                # Create offline_tiles directory if it doesn't exist
                os.makedirs(os.path.join(destination_dir, "offline_tiles"), exist_ok=True)
                
                # Copy and convert the file
                print(f"Converting: {source_file} -> {dest_file}")
                shutil.copy2(source_file, dest_file)

# Kullanım
source_dir = r"C:\Users\PC_6270\Desktop\examplemapsatt"
destination_dir = r"C:\Users\PC_6270\Desktop\newOSMTiles"

try:
    convert_tiles(source_dir, destination_dir)
    print("Dönüştürme işlemi tamamlandı!")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
