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

`Include /gpfs22/home/mcarthe/folder_for_readme in README? (y/n)`

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

