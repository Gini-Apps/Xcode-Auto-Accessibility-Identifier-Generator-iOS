import os
import uuid
import time
from accessibility import add_accessibility_if_needed
from concurrent.futures.thread import ThreadPoolExecutor

project_path  = ""
all_files = []
ui_files_path = []

start = time.time()

# get all files path and save
for dir_, _, files in os.walk(project_path):
    for file_name in files:
        rel_dir = os.path.relpath(dir_, project_path)
        rel_file = os.path.join(project_path, rel_dir, file_name)
        all_files.append(rel_file)

# filter all files and get only UI files
for file in all_files:
    if file.endswith('.xib') or file.endswith('.storyboard'):
        ui_files_path.append(file)

# run def "add_accessibility_if_needed" in parallel tasks
with ThreadPoolExecutor(max_workers=len(ui_files_path)) as executor:
    for xml_path in ui_files_path:
        executor.submit(add_accessibility_if_needed, xml_path)

end = time.time()

print("Time execution {0}".format(end - start))


    
