# first import os
"""
import os
os.remove('C:/Users/Nzilani/Downloads/out.txt')
# so this code also deletes and the one below first check if it exist and then deletes
"""

# to check if the file exists 
import os

file_path = 'C:/Users/Nzilani/Downloads/out.txt'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The file does not exist")


# to delete an entire foler we  ose rmdir

import os
os.rmdir('C:/Users/Nzilani/Downloads/afolder')