import os, shutil, time

def CP (src, dest, t):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            time.sleep(t)

# src = '/home/asura-ubuntu/arutest/image_fold/8'
# dest = '/home/asura-ubuntu/arutest/image_fold/2'
# t = 3

# CP(src, dest, t)
