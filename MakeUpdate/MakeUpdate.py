#!/usr/bin/python3

import os
import os.path
import shutil
import filecmp
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


def getPath(path, oldFolder, newFolder, targetFolder):
    path = os.path.relpath(path, newFolder)
    oldFile = os.path.join(oldFolder, path)
    newFile = os.path.join(newFolder, path)
    targetFile = os.path.join(targetFolder, path)
    return (path, oldFile, newFile, targetFile)


def makeUpdate(oldFolder, newFolder, targetFolder):
    for root, dirs, files in os.walk(newFolder):
        for folder in dirs:
            path, oldFile, newFile, targetFile = getPath(os.path.join(
                root, folder), oldFolder, newFolder, targetFolder)
            if(not os.path.exists(oldFile) and not os.path.exists(targetFile)):
                print("Create folder: " + path)
                os.makedirs(targetFile)
        for file in files:
            path, oldFile, newFile, targetFile = getPath(os.path.join(
                root, file), oldFolder, newFolder, targetFolder)
            if (not os.path.exists(oldFile) or not filecmp.cmp(newFile, oldFile)):
                if (not os.path.exists(os.path.dirname(targetFile))):
                    os.makedirs(os.path.dirname(targetFile))
                print("Copy file: " + path)
                shutil.copyfile(newFile, targetFile)


Tk().geometry("+99999+99999")  # hide main window

oldFolder = filedialog.askdirectory(title='Select old folder')
if(oldFolder == ""):
    exit(0)

newFolder = filedialog.askdirectory(initialdir=os.path.dirname(
    oldFolder), title='Select new folder')
if(newFolder == ""):
    exit(0)

targetFolder = filedialog.askdirectory(
    initialdir=os.path.dirname(newFolder), title='Select target folder', mustexist=False)
if(targetFolder == ""):
    exit(0)

makeUpdate(oldFolder, newFolder, targetFolder)
messagebox.showinfo("Make Update", "Completed!")
