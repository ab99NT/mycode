#!/usr/bin/env python3

import shutil

import os

def main():

#Change to the directory listed
    os.chdir("/home/student/mycode/")

#Copy file between directories
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#Copy directory structure
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":

    main()
