#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, shutil, time

class CP:
    def CopyFiles(self, src, dest, timeset=1):
        # self.src = src
        # self.dest = dest
        # self.timeset = timeset

        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest)
                time.sleep(timeset)

# CP.CopyFiles('/home/asura-ubuntu/arutest/image_fold/8','/home/asura-ubuntu/arutest/image_fold/3',1)
