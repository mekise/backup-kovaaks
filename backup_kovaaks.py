# to build the executable:
# >>> pip install pyinstaller
# >>> pyinstaller -F copy_files_to_folder.py
# the files are created in mekise/dist/

import shutil, os
from pathlib import Path

p = Path.home()

source_folder = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\FPSAimTrainer\\FPSAimTrainer\\stats"
target_folder = p / "My Drive\\gaming\\kovaak_backup\\stats"

file_names = os.listdir(source_folder)

os.makedirs(target_folder, exist_ok = True)

for file_name in file_names:
    if file_name.endswith('.csv'):
        shutil.copy(os.path.join(source_folder, file_name), target_folder)