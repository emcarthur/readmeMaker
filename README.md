# readmeMaker
python script to create and edit README files

<b>Installation</b>

Copy or clone the readmeMaker into your home directory of choice
Make readmeMaker.py executable:
```
chmod + readmeMaker/readmeMaker.py
```
Make this folder searchable via your PATH. Add this line to your .bashrc file and source it: 
```
PATH=/my/home/directory/readmeMaker/:$PATH
source .bashrc
```
In the readmeMaker.py script itself, change the name on line 32 to your own
```
Creator: Your Name Here
```
<b>Usage</b>

Navigate to the folder you want to create a README for and run the readmeMaker.py. Add your project description/usage and tell readmeMaker what folders/files you care about:



`[folder_for_readme]$ readmeMaker.py
Project title:`

readmeMaker for GitHub

`Project description:`

How to use the ReadmeMaker.py

`Usage:`

Use scripts from folderB on data from folderA

`Include /home/mcarthe/folder_for_readme in README? (y/n)`

y

`Describe the function/usage of (or 'rm' to ignore) file: README`

An awesome README!

`Include /home/mcarthe/folder_for_readme/folderA in README? (y/n)`

y

`Describe the function/usage of (or 'rm' to ignore) file: some_other_cool_stuff.bed`

A bed file with cool stuff

`Describe the function/usage of (or 'rm' to ignore) file: i_dont_care_about.this`

rm  #this means 'i_dont_care_about.this' won't show up in README

`Describe the function/usage of (or 'rm' to ignore) file: some_raw_data.txt`

The data from google.com

`Include /home/mcarthe/folder_for_readme/folderB in README? (y/n)`

y

`Describe the function/usage of (or 'rm' to ignore) file: script_for_fun.py`

python scripts are fun


<b>Example output:</b>
```
################
Creator: Evonne McArthur
Created: 2018-10-18
Updated:
Title:   readmeMaker for GitHub
About:   How to use the ReadmeMaker.py
Usage:   Use scripts from folderB on data from folderA
################


MANIFEST
################

## /home/mcarthe/folder_for_readme ##
README  An awesome README!

## /home/mcarthe/folder_for_readme/folderA ##
some_other_cool_stuff.bed       A bed file with cool stuff
some_raw_data.txt       The data from google.com

## /home/mcarthe/folder_for_readme/folderB ##
script_for_fun.py       python scripts are fun
```

<b> Edit your existing README </b>
If you run readmeMaker.py in a folder that already has a README, you will be prompted to either edit or overwrite the file. If you choose to edit the file, it will date stamp your README with the date and it will compare your previous manifest with the current file directory manifest. It will remove anything you've deleted from your manifest from the README and prompt you to describe any new files to add to the updated README.
