print ("This is the Beginning")

import numpy as np
import os
import datetime
from time import sleep
import shutil
dir = os.path.dirname(os.path.abspath(__file__))

def mockMicroscope():
    startDirSize= dirSize(dir)

    src= dir + '/ExampleImage.tif' 
    dest= dir + '/ExampleImage2.tif' 

    input_name= 'ExampleImage.tif'
    time =  str(datetime.datetime.now())
    Hour,Min,Sec = os.path.basename(time).split(':')
    print (time)

    print ("File Replication Step")
    time =  str(datetime.datetime.now())
    starttime =  (datetime.datetime.now())
    Hour,Min,Sec = os.path.basename(time).split(':')
    print (time)
    for step in range(1,10):
      sleep(0.0001)
      time =  str(datetime.datetime.now())
      T = str(step)
      Hour,Min,Sec = os.path.basename(time).split(':')
      dirname= dir +'/' + T +'folder/'
      try:
        os.stat(dirname)
      except:
        os.mkdir(dirname) 
      os.chdir(dirname)

      for x in range(1,100):
       time =  str(datetime.datetime.now())
       X = str(x)
       Hour,Min,Sec = os.path.basename(time).split(':')
       # outputname = dir+\+ X +'folder'
       # shutil.copyfile(src, outputname)
       # print (outputname)
       # print ("Hello fellow Python classmates!")
       dest=dirname+Sec+'Image.tif'
       #print (src)
       #print (dest)
       shutil.copyfile(src,dest)
    time =  str(datetime.datetime.now())
    Hour,Min,Sec = os.path.basename(time).split(':')
    print (time)
    finishtime =  (datetime.datetime.now())
    timespent= str(finishtime-starttime)
    print ("Replication Finished in" , timespent , 'sec' )

    #FinalDirStats=os.stat(dir)

    #FileSize= FinalDirStats.st_size - StartDirStats.st_size 
    #print (FinalDirStats)
    #print (StartDirStats)
    return dirSize(dir) - startDirSize  #finish - start

    print ('This is the end')

def dirSize(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def main():
    fname = dir + "/init.txt"
    if not os.path.isfile(fname):
        fSize = mockMicroscope()
        target = open(fname, 'w')
        target.write(str(fSize))
    else:
      target = open(fname, 'r')
      fSize = int(target.readline())
    print fSize
if __name__ == "__main__":
    main()
"""
# To do

1. Adjust file generation script to match Microscope generation rate and structure.  Mock files as being in use.  

2. Create analytics to measure directory size before and after.

3. Create monitor to determine if a file(or directory) is complete and/or in use.

4a & 5a.   Globus may be able to handle these steps.

4. Create Copy command to replicate files that are complete from local storage to RDSS or FSMresfiles.

5. Create monitor to determine that files have veen replicated from local storage to desitiation successfully.

6.  Delete local files after status has been confirmed.


For Alper and Aaron (and David)

Determine if CAM&NIC will use globus.
Determine split of files and folders. 
Determine ultimate location of folders and associated permissions per user. 

"""