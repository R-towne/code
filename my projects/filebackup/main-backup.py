import os 
import shutil
#to pull the date for the new file 
from datetime import date
todaysdate=date.today()
#to copy files into the new folder 
copypath='/run/media/ryan_towne/main drive'
src='/home/ryan_towne/Documents/vscode'
dest = "/run/media/ryan_towne/main drive/code-saves/code-{}".format(todaysdate)
copy=shutil.copytree(src,dest, dirs_exist_ok=True)
#print to see when done and completed 
print('----------------------------------------')
print('done')
print('----------------------------------------')
print(dest)
print('----------------------------------------')