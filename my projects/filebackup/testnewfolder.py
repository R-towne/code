import os 
import shutil

#to get the date 
from datetime import date
todaydate=date.today()

newFolder =(str(todaydate))
 
parent_dir = "/run/media/ryan_towne/test usb"
 
path = os.path.join(parent_dir, newFolder) 

os.mkdir(path) 
print("Directory '% s' created" % newFolder) 
