import os, shutil, time

# class CP:
#     def FindFiles(self, src):
#         self.src = src
#
#         src_files = os.listdir(self.src)
#         for file_name in src_files:
#             full_file_name = os.path.join(self.src, file_name)
#             return full_file_name
#
#     def CopyFiles(self, dest, t):
#         self.dest = dest
#         self.t = t
#
#         if os.path.isfile(full_file_name):
#             shutil.copy(full_file_name, self.dest)
#             time.sleep(self.t)

def CP (src, dest, t):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            time.sleep(t)

# src = '/home/asura-ubuntu/arutest/image_fold/3'
# dest = '/home/asura-ubuntu/arutest/image_fold/1'
# t = 1

# CP.FindFiles(src)
# CP.CopyFiles(dest,t)
# CP(src, dest, t)
