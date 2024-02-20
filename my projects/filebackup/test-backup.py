import os 
import shutil

#to pull the date for the new file 
from datetime import date
todaysdate=date.today()

#to copy the file  
copypath='place the wanted file is in'
src='the wanted file'
dest = "to put this file in{}".format(todaysdate)
copy=shutil.copytree(src,dest, dirs_exist_ok=True)

#print to see when done and completed 
print('done')
print(dest)