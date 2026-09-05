from pathlib import Path
import shutil

folder = Path("test_files")

print("Files found:")

for file in folder.iterdir():
    print(file.name)
