#prints the absolute path name of the current working directory.
0-current_working_directory
!#/bin/bash
pwd

#Display the contents list of your current directory.
1-listit
!#/bin/bash
ls

#working directory to the user’s home directory. 
2-bring_me_home
!#/bin/bash
cd ~

#Display current directory contents in a long format


3-listfiles 
!#/bin/bash
ls -l

#Display current directory contents, including hidden files (starting with .). Use the long format.
4-listmorefiles
!#/bin/bash
ls-al

#Display current directory contents.
Long format
with user and group IDs displayed numerically
And hidden files (starting with .)
5-listfilesdigitonly 
!#/bin/bash

#creates a directory named my_first_directory in the /tmp/ directory.
6-firstdirectory 
!#/bin/bash

#Move the file betty from /tmp/ to /tmp/my_first_directory
7-movethatfile
!#/bin/bash

#Delete the file betty.
8-firstdelete
!#/bin/bash

#Delete the directory my_first_directory that is in the /tmp directory.
9-firstdirdeletion
!#/bin/bash

#Write a script that changes the working directory to the previous one
10-back
!#/bin/bash

#lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format
11-lists
!#/bin/bash

#prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script
12-file_type
!#/bin/bash

13-symbolic_link 
!#/bin/bash

14-copy_html
!#/bin/bash
