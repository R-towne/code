import shutil
import os

path="/home/ryan_towne/Documents"
src="/run/media/ryan_towne/test usb/test1"
dest="/run/media/ryan_towne/test usb/test2"

copy=shutil.copytree(src,dest, dirs_exist_ok=True)

#SECTION - main code 
print('-------------------------------------------------------------------------------------------------------')
print(src)
print('-------------------------------------------------------------------------------------------------------')
print(dest)
print('-------------------------------------------------------------------------------------------------------')
#before the script run
print('before copying files')
print(os.listdir(path))
print('-------------------------------------------------------------------------------------------------------')
#after the script run
print('after copying')
print("copy path",copy)
print('-------------------------------------------------------------------------------------------------------')