#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" readmeMaker.py: Makes a readme file for project folders """

__author__ = 'Evonne McArthur'
__date__ = '10/8/2018'

import pathlib
import datetime
import os

now = datetime.datetime.now()

exists = pathlib.Path('README')

if exists.exists(): # determine if you want to just overwrite or edit
    print('A README already exists. Respond \'e\' to edit existing file and \'o\' to overwrite')
    edit = input()
if not exists.exists() or edit == 'o':  # write new readme or overwrite existing
    f_out = open('README', 'w')

    # input for header:
    print('Project title:')
    title = input()
    print('Project description:')
    about = input()
    print('Usage:')
    usage = input()

    f_out.write("""################
Creator: Evonne McArthur
Created: """ + now.strftime("%Y-%m-%d") + """
Updated:
Title:   """ + title + """
About:   """ + about + """
Usage:   """ + usage + """
################\n\n
MANIFEST
################\n""")

    for (path, dirs, files) in os.walk(os.getcwd()): # walk through files in directory
        if not path.lstrip().startswith('.') and '/.' not in path:
            print('Include ' + path + ' in README? (y/n)') # do you want to include the folder?
            path_include = input()
            if path_include == 'y':
                f_out.write('\n## ' + path + ' ##\n') # print folder name
                for f in files:
                    if not f.lstrip().startswith('.'):
                        print('Describe the function/usage of (or \'rm\' to ignore) file: ' \
                                    + f.lstrip())
                        file_descrip = input() # get file description
                        if not(file_descrip == 'rm'):
                            f_out.write(f.lstrip() + '\t'
                                    + file_descrip + '\n')

else: # edit existing readme
    exists = pathlib.Path('tmp')

    if exists.exists():
        print('You have a folder \'tmp\' in this directory. This program will delete that file so remove/rename it before running again. Exiting now.')
        exit()
    f_in = open('README', 'r')
    f_out = open('tmp', 'w')
    manifest = {}
    in_manifest = False
    for line in f_in.readlines():

        if line.lstrip().startswith('Updated:') & (not in_manifest): # add the current  date to the updated section
            f_out.write(line.strip('\n') + ' ' + now.strftime('%Y-%m-%d'
                        ) + ',\n')
        elif line.lstrip().startswith('MANIFEST') & (not in_manifest):
            in_manifest = True # now in the manifest portion of the readme
            f_out.write(line)
            f_out.write('################\n')
        elif not in_manifest:
            f_out.write(line) # copy header lines
        elif in_manifest:
            file_in_manifest = line.lstrip().strip('\n').split('\t', 1) # split the file from the file description
            if len(file_in_manifest) == 2: # if the file already has a description
                manifest[file_in_manifest[0]] = file_in_manifest[1] # add description to dictionary for file key
            else:
                manifest[file_in_manifest[0]] = ''

    for (path, dirs, files) in os.walk(os.getcwd()): # walk through files in directory
        if not path.lstrip().startswith('.') and '/.' not in path:
            print('Include ' + path + ' in README? (y/n)') # do you want to include the folder
            path_include = input()
            if path_include == 'y':
                f_out.write('\n## ' + path + ' ##\n') # print folder name
                for f in files:
                    file_in_manifest = f.lstrip().strip('\n')
                    if not(file_in_manifest.startswith('.')) and not(file_in_manifest == 'tmp'):
                        if file_in_manifest in manifest: # if the file in directory already exists in manifest dict
                            if manifest[file_in_manifest] == "": # if description is empty
                                print('Describe the function/usage of (or \'rm\' to ignore) file: ' \
                                    + f.lstrip() + ':')
                                file_descrip = input()
                                if not(file_descrip == 'rm'):
                                    f_out.write(file_in_manifest + '\t'
                                        + file_descrip + '\n')
                            else:
                                f_out.write(file_in_manifest + '\t'
                                    + manifest[file_in_manifest] + '\n')
                        else: # if the file in directory did not exist already, ask for function
                            print('Describe the function/usage of (or \'rm\' to ignore) file ' \
                                + file_in_manifest + ':')
                            file_descrip = input()
                            if not(file_descrip == 'rm'):
                                f_out.write(file_in_manifest + '\t'
                                        + file_descrip + '\n')
    f_in.close()
    f_out.close()

    open('README', 'w').writelines([l for l in open('tmp').readlines()]) # move tmp file to README
    os.remove('tmp')

f_out.close()
