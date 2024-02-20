import os 
import shutil
#to pull the date for the new file 
from datetime import date
todaysdate=date.today()
#to copy files into the new folder 
copypath='/run/media/ryan-laptop/main drive'
src='/home/ryan-laptop/Documents/vscode'
dest = "/run/user/1000/gvfs/smb-share:server=truenas.local,share=main-storage/codecode-{}".format(todaysdate)
copy=shutil.copytree(src,dest, dirs_exist_ok=True)
#print to see when done and completed 
print('----------------------------------------')
print('done')
print('----------------------------------------')
print(dest)
print('----------------------------------------')